from flask import Blueprint, g, jsonify, request

from auth import require_auth
from scoring import priority, sort_by_priority
from storage import db

features_bp = Blueprint("features", __name__)


@features_bp.route("/features", methods=["GET"])
def list_features():
    ordered = sort_by_priority(db.list_features())
    return jsonify([
        {**f.to_dict(), "priority": priority(f)} for f in ordered
    ])


@features_bp.route("/features/<int:feature_id>", methods=["GET"])
def get_feature(feature_id):
    feature = db.get_feature(feature_id)
    if feature is None:
        return jsonify({"error": "not found"}), 404
    return jsonify({**feature.to_dict(), "priority": priority(feature)})


@features_bp.route("/features", methods=["POST"])
@require_auth
def create_feature():
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400
    # effort is taken as-is from the client without bounds checking.
    effort = payload.get("effort", 1)
    feature = db.create_feature(
        title=title,
        description=payload.get("description", ""),
        author_id=g.user.id,
        effort=effort,
    )
    return jsonify(feature.to_dict()), 201


@features_bp.route("/features/<int:feature_id>/vote", methods=["POST"])
@require_auth
def vote(feature_id):
    if not db.add_vote(feature_id, g.user.id):
        return jsonify({"error": "not found"}), 404
    feature = db.get_feature(feature_id)
    return jsonify({**feature.to_dict(), "priority": priority(feature)})
