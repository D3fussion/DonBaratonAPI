from flask import session, jsonify
from psycopg2.extras import RealDictCursor
from functions.get_db_connection import get_db_connection

def login(data):
    email = data.get('email')
    password = data.get('password')
    print(email, password)

    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SET search_path TO "MercadoOnline";')

    # Verificar si el email y la contraseña coinciden con algún usuario en la base de datos
    cursor.execute('SELECT * FROM usuarios WHERE email = %s AND password = %s', (email, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        session['logged_in'] = True
        session['user_email'] = email
        return jsonify(
            {"message": "Login successful", "logged_in": session['logged_in'], "email": session['user_email']}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401