from flask import jsonify, session


def is_logged_in():
    if 'logged_in' in session and session['logged_in']:
        return jsonify({"logged_in": True, "user_email": session['user_email']})
    else:
        return jsonify({"logged_in": False, "session": session})
