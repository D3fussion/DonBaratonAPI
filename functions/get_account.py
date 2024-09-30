from flask import jsonify, session
from psycopg2.extras import RealDictCursor
from functions.get_db_connection import get_db_connection

def get_account():
    email = session.get('user_email')  # Obtener el email desde la sesión
    if not email:
        return jsonify({"message": "User not logged in"}), 401  # Si no está logueado
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    # Buscar la cuenta del usuario en la base de datos
    cursor.execute("SELECT email, first_name, last_name, address, addInfo, phone_number FROM usuarios WHERE email = %s",
                   (email,))
    account = cursor.fetchone()
    conn.close()
    if account:
        print(account)
        return jsonify(account), 200  # Devolver la información de la cuenta
    else:
        session.pop('user_email', None)
        return jsonify({"message": "Account not found"}), 404  # Si no encuentra la cuenta
