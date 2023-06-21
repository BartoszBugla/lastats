from flask_restx import Resource
from flask import Response, request

from http import HTTPStatus

from api.extensions import db
from api.models.team import Team

from .dto.team_dto import *
from .dto.base_models import *

MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "Team not found"

teams = {
    0: {"id": 0, "name": "Team Alpha", "league_id": 1, "league_points": 12},
    1: {"id": 1, "name": "Team Bravo", "league_id": 1, "league_points": 10},
    2: {"id": 2, "name": "Team Charlie", "league_id": 1, "league_points": 8},
}


@teams_ns.route("teams")
class Teams(Resource):
    @classmethod
    @teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [team_model])
    @teams_ns.marshal_list_with(team_model)
    def get(cls):
        """
        Returns list of all the teams whose names contain the given query.
        """
        return Team.query.all()

    @classmethod
    @teams_ns.response(HTTPStatus.CREATED, MESSAGE_SUCCESS)
    @teams_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @teams_ns.response(HTTPStatus.CONFLICT, "CONFLICT")
    @teams_ns.expect(create_team_request)
    def post(cls):
        """
        Creates a new team.
        """
        data: dict = request.json

        new_team = Team(
            data["name"],
            data["league_points"] if "league_points" in data else None,
            data["wins"] if "wins" in data else None,
            data["draws"] if "draws" in data else None,
            data["losses"] if "losses" in data else None,
        )
        db.session.add(new_team)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)


@teams_ns.route("teams/<int:team_id>")
class TeamById(Resource):
    @classmethod
    @teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, team_model)
    @teams_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @teams_ns.marshal_with(team_model)
    def get(cls, team_id):
        """
        Returns the team with the specified ID.
        """
        return Team.query.get(team_id)

    @classmethod
    @teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @teams_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @teams_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @teams_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    @teams_ns.expect(create_team_request)
    def put(cls, team_id):
        """
        Updates league's data.
        """
        data = request.json

        team: Team = Team.query.get_or_404(team_id)

        team.name = data["name"] if "name" in data else team.name

        db.session.commit()

        return "League updated"

    @classmethod
    def delete(cls, team_id):
        """
        Deletes the team with the specified ID.
        """
        team: Team = Team.query.get_or_404(team_id)

        db.session.delete(team)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)
