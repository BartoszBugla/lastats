from flask import Blueprint, Response, jsonify, request


teams_bp = Blueprint("teams", __name__)


@teams_bp.get("/")
def get_teams():
    return teams


@teams_bp.post("/")
def add_team():
    team = {"name": request.form.get("name"), "id": len(teams["teams"]) + 1}

    teams["teams"].append(team)

    return Response(status=201)


@teams_bp.put("/<int:id>")
def update_team(id):
    team = teams["teams"][id]
    team["name"] = request.form.get("name")

    return Response(status=200)


@teams_bp.delete("/<int:id>")
def delete_team(id):
    teams["teams"].pop(id)

    return Response(status=200)
