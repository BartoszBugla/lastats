from flask import Blueprint, jsonify

from app.services.test_service import create_test, get_all


test_bp = Blueprint("test", __name__)


@test_bp.route("/create", methods=["GET"])
def create():
    id = create_test()
    return jsonify({"id": id})


@test_bp.route("/", methods=["GET"])
def get_all_items():
    return jsonify(get_all())
