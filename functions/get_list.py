from flask import jsonify
from psycopg2.extras import RealDictCursor
from functions.get_db_connection import get_db_connection


def get_list(data):
    search_term = data.get('search_term').replace("-", " ").replace("=", "")
    print(search_term)

    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    response = []

    # Si el término de búsqueda está vacío, devuelve todos los productos
    if search_term == "":
        cursor.execute("SELECT * FROM productos")
        products = cursor.fetchall()
        response.extend(products)

    # Si el término es "$First5", devuelve los primeros 5 productos
    elif search_term == "$First5":
        cursor.execute("SELECT * FROM productos LIMIT 5")
        products = cursor.fetchall()
        response.extend(products)

    # Si el término empieza con "%24Categoria", busca por categoría
    elif search_term[0:12] == "%24Categoria":
        if search_term[12:] == "":  # Si no hay categoría especificada, devuelve todos los productos
            cursor.execute("SELECT * FROM productos")
            products = cursor.fetchall()
            response.extend(products)
        else:
            categoria_id = int(search_term[12:])
            cursor.execute("SELECT * FROM productos WHERE categorias = %s", (categoria_id,))
            products = cursor.fetchall()
            response.extend(products)

    # Si el término es un ID o una coincidencia por nombre
    else:
        if search_term.isdigit():  # Si el término es un número, busca por ID
            cursor.execute("""
                                SELECT p.*, c.nombre_categoria 
                                FROM productos p 
                                LEFT JOIN categorias c ON p.categorias = c.id 
                                WHERE p.id = %s
                            """, (int(search_term),))
            product = cursor.fetchone()
            if product:
                response.append(product)
        else:  # Si no es número, busca por nombre
            cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) LIKE %s", ('%' + search_term.lower() + '%',))
            products = cursor.fetchall()
            response.extend(products)

    conn.close()
    print(response)
    return jsonify(response)
