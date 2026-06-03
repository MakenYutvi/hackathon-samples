"""Token-based authentication helpers.

The token is passed in the `X-Token` header. This is intentionally simple:
there is no expiry, no rotation, and tokens are compared as plain strings.
"""
from functools import wraps

from flask import g, jsonify, request

from storage import db


def current_user():
    token = request.headers.get("X-Token", "")
    return db.user_by_token(token)


def require_auth(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        user = current_user()
        if user is None:
            return jsonify({"error": "unauthorized"}), 401
        g.user = user
        return view(*args, **kwargs)

    return wrapper
