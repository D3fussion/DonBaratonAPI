from flask import Flask, request
from flask_cors import CORS
from flask_session import Session
import functions
import redis

app = Flask(__name__)
app.secret_key = '^gK2V^_Qd?10'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379)
Session(app)
CORS(app, supports_credentials=True)


@app.route('/get_products', methods=['POST'])
def get_products():
    data = request.json
    print(data)
    return functions.get_products(data)


@app.route('/place_order', methods=['POST'])
def place_order():
    order_data = request.json
    print(order_data)
    return functions.place_order(order_data)


@app.route('/get_list', methods=['POST'])
def get_list():
    data = request.json
    print(data)
    return functions.get_list(data)


@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Email y Contraseña
    print(request.cookies)
    return functions.login(data)


@app.route('/is_logged_in', methods=['GET'])
def is_logged_in():
    print(request.cookies, "hola soy las cookies")
    return functions.is_logged_in()


@app.route('/get_account', methods=['GET'])
def get_account():
    return functions.get_account()


@app.route('/update_account', methods=['POST'])
def update_account():
    data = request.json
    print(data)
    return functions.update_account(data)


@app.route('/log_out', methods=['GET'])
def log_out():
    return functions.log_out()


@app.route('/set_order_code', methods=['GET'])
def set_order_code():
    return functions.set_order_code()


@app.route('/get_order_code', methods=['GET'])
def get_order_code():
    return functions.get_order_code()


@app.route('/get_orders', methods=['GET'])
def get_orders():
    return functions.get_orders()


if __name__ == '__main__':
    app.run()
