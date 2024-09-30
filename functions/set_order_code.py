import random
from flask import session, jsonify
from functions.get_db_connection import get_db_connection

def set_order_code():
    codigo = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
    session['lastOrder'] = codigo
    print(session['lastOrder'])
    return jsonify({"code": codigo}), 200