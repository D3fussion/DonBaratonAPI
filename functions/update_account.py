from flask import jsonify, session
from functions.get_db_connection import get_db_connection


def update_account(data):
    email = session.get('user_email')  # Obtener el email de la sesión
    if not email:
        return jsonify({"message": "User not logged in"}), 401  # Si no está logueado

    print(email)
    print(data)

    # Crear una lista de campos y valores para actualizar
    update_fields = []
    update_values = []

    # Actualizar solo los campos enviados en el request
    if 'first_name' in data:
        update_fields.append('first_name = %s')
        update_values.append(data['first_name'])
    if 'last_name' in data:
        update_fields.append('last_name = %s')
        update_values.append(data['last_name'])
    if 'address' in data:
        update_fields.append('address = %s')
        update_values.append(data['address'])
    if 'addInfo' in data:
        update_fields.append('addInfo = %s')
        update_values.append(data['addInfo'])
    if 'phone_number' in data:
        update_fields.append('phone_number = %s')
        update_values.append(data['phone_number'])
    if 'password' in data:
        if not data['password'] == "":
            update_fields.append('password = %s')
            update_values.append(data['password'])

    # Verificar si hay datos para actualizar
    if not update_fields:
        return jsonify({"message": "No data provided for update"}), 400

    update_values.append(email)  # Añadir el email al final para la condición WHERE

    # Formar la consulta SQL
    update_query = f"UPDATE usuarios SET {', '.join(update_fields)} WHERE email = %s"

    # Conectar a la base de datos y ejecutar la actualización
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SET search_path TO "MercadoOnline";')

    cursor.execute(update_query, update_values)
    conn.commit()

    # Verificar si alguna fila fue actualizada
    if cursor.rowcount > 0:
        conn.close()
        return jsonify({"message": "Account updated successfully"}), 200
    else:
        conn.close()
        return jsonify({"message": "Account not found"}), 404