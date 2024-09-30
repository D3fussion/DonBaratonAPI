from flask import jsonify
from psycopg2.extras import RealDictCursor
from functions.get_db_connection import get_db_connection


def get_products(data):
    cart_items = data.get('products', [])

    if not cart_items:
        return jsonify({"message": "No products in the cart"}), 400

    product_ids = [int(item['id']) for item in cart_items]

    # Conectar a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Obtener los productos de la base de datos cuyas IDs coinciden con las del carrito
    query = "SELECT id, nombre, precio_despues_descuento, link_imagen1, stock_disponible FROM productos WHERE id = ANY(%s)"
    cursor.execute(query, (product_ids,))
    products = cursor.fetchall()

    response = []

    # Crear la respuesta incluyendo la cantidad solicitada de cada producto
    for product in products:
        for item in cart_items:
            if int(item['id']) == product['id']:
                product_info = {
                    "id": product['id'],
                    "nombre": product['nombre'],
                    "precio_despues_descuento": product['precio_despues_descuento'],
                    "link_imagen1": product['link_imagen1'],
                    "stock_disponible": product['stock_disponible'],
                    "quantity": item['quantity']
                }
                response.append(product_info)

    conn.close()
    print(response)
    return jsonify(response)
