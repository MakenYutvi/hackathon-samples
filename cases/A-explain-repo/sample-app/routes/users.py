from flask import Blueprint, jsonify, request

from storage import db

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400
    user = db.create_user(name)
    # The token is returned in plaintext so the demo client can store it.
    return jsonify({"id": user.id, "name": user.name, "token": user.token}), 201
