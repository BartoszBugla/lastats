from flask import Blueprint, jsonify, request

from api.extensions import db
from api.models.league import League
from api.utils import serialize_all

league_bp = Blueprint("leagues", __name__)


@league_bp.route("/", methods=["GET"])
def get_all():
    leagues = serialize_all(League.query.all())

    return jsonify(leagues)


@league_bp.route("/", methods=["POST"])
def add_league():
    data = request.form.get("name")

    new_league = League(name=data)

    db.session.add(new_league)
    db.session.flush()
    db.session.commit()

    return jsonify({"id": new_league.id})


@league_bp.route("/<int:id>", methods=["PUT"])
def update_league(id):
    League.query.filter_by(id=id).update({"name": request.form.get("name")})

    db.session.commit()

    return jsonify({"id": id})


@league_bp.route("/<int:id>", methods=["DELETE"])
def delete_league(id):
    League.query.filter_by(id=id).delete()

    db.session.commit()

    return jsonify({"id": id})


@league_bp.route("/<int:id>", methods=["DELETE"])
def get_by_id(id):
    league = League.query.filter_by(id=id)

    return league.to_json()
