from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload

from api.extensions import db
from api.models.league import League
from api.models.team import Team
from api.utils import serialize_all

league_bp = Blueprint("leagues", __name__)


@league_bp.route("/", methods=["GET"])
def get_all():
    leagues = serialize_all(League.query.all())

    print(leagues)
    return jsonify(leagues)


@league_bp.route("/", methods=["POST"])
def add_league():
    data = request.json

    new_league = League(name=data["name"])

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


@league_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id: int):
    league: League = League.query.get_or_404(id)

    serialized = league.serialize()
    serialized["teams"] = serialize_all(league.teams)

    return jsonify(serialized)


@league_bp.route("/<int:id>/teams", methods=["POST"])
def update_teams(id: int):
    league: League = League.query.get_or_404(id)

    ids = tuple(request.json["ids"])

    for id in ids:
        Team.query.filter_by(id=id).update({"league_id": league.id})

    db.session.commit()

    return jsonify({"id": "gege"})
