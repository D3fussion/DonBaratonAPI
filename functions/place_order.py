import json
from flask import jsonify
from functions.get_db_connection import get_db_connection


def place_order(order_data):
    email_usuario = order_data.get('email_usuario')
    productos = order_data.get('productos')  # Formato: [{"id":"13","cantidad":1,"nombre":"Bananas"}, {"id":"12","cantidad":1,"nombre":"Bananas"}]
    productos_no_str = json.loads(productos)
    print(productos_no_str)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SET search_path TO "MercadoOnline";')

    # Generate a unique tracking code and insert the order
    codigo_trackeo = order_data.get('codigo_trackeo')

    values = []
    for i in productos_no_str:
        values.append((email_usuario, codigo_trackeo, i['id'], i['cantidad'], i['nombre']))

    sql = "INSERT INTO ordenes (email_usuario, codigo_trackeo, producto, cantidad, nombre) VALUES %s"
    args_str = ','.join(cursor.mogrify("(%s, %s, %s, %s, %s)", x).decode('utf-8') for x in values)
    cursor.execute(sql % args_str)

    # Build the UPDATE query with CASE
    update_query = "UPDATE productos SET stock_disponible = CASE"
    ids = []
    for i in productos_no_str:
        update_query += f" WHEN id = %s THEN stock_disponible - %s"
        ids.extend([i['id'], i['cantidad']])
    update_query += " END WHERE id IN %s"

    cursor.execute(update_query, (*ids, tuple(i['id'] for i in productos_no_str)))

    conn.commit()
    conn.close()

    return jsonify({"message": "Order placed successfully"}), 200
