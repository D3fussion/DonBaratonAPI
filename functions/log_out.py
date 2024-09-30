from flask import jsonify, session


def log_out():
    session.clear()
    return jsonify({"message": "Logged out"}), 200