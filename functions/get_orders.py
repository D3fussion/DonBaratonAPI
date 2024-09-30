from flask import session, jsonify
from psycopg2.extras import RealDictCursor
from functions.get_db_connection import get_db_connection

def get_orders():
    email = session.get('user_email')
    if not email:
        return jsonify({"message": "User not logged in"}), 401
    else:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('SET search_path TO "MercadoOnline";')
        cursor.execute("SELECT * FROM ordenes WHERE email_usuario = %s", (email,))
        orders = cursor.fetchall()
        print(orders)
        conn.close()
        return jsonify(orders), 200