from flask import jsonify, session


def get_order_code():
    return jsonify({"code": session["lastOrder"]}), 200