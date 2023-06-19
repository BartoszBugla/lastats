from flask_restx import Resource
from flask import Response, request

from http import HTTPStatus

from api.models.team import Team

from .dto.teams import *

MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "Team not found"

teams = {
    0: {"id": 0, "name": "Team Alpha", "league_id": 1, "league_points": 12},
    1: {"id": 1, "name": "Team Bravo", "league_id": 1, "league_points": 10},
    2: {"id": 2, "name": "Team Charlie", "league_id": 1, "league_points": 8},
}


@teams_ns.route("teams")
class ListAllTeams(Resource):
    @classmethod
    @teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [team_model])
    @teams_ns.marshal_list_with(team_model)
    def get(cls):
        """
        Returns list of all the teams whose names contain the given query.
        """
        return Team.query.all()


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
        if team_id not in teams:
            return Response(status=HTTPStatus.NOT_FOUND)

        return Response(response=teams[team_id], status=HTTPStatus.OK)

    @classmethod
    @teams_ns.response(HTTPStatus.CREATED, MESSAGE_SUCCESS)
    @teams_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @teams_ns.response(HTTPStatus.CONFLICT, "CONFLICT")
    @teams_ns.expect(create_team_request)
    def post(cls, team_id):
        """
        Creates a new team.
        """
        data = request.json
        if not data:
            return Response(status=HTTPStatus.BAD_REQUEST)

        if team_id in teams:
            return Response(status=HTTPStatus.CONFLICT)

        name = data["name"]
        teams[team_id] = {"id": team_id, "name": name}

        return Response(status=HTTPStatus.CREATED)

    @classmethod
    @teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @teams_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @teams_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @teams_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    def put(cls, team_id):
        """
        Updates team's data.
        """
        data = request.json
        if not data:
            return Response(status=HTTPStatus.BAD_REQUEST)

        if team_id not in teams:
            return Response(status=HTTPStatus.NOT_FOUND)

        name = data["name"]
        if name:
            teams[team_id]["name"] = name
            return Response(status=HTTPStatus.OK)

        return Response(status=HTTPStatus.NO_CONTENT)

    @classmethod
    def delete(cls, team_id):
        """
        Deletes the team with the specified ID.
        """
        if team_id not in teams:
            return Response(status=HTTPStatus.NOT_FOUND)

        teams.pop(team_id)
        return Response(status=HTTPStatus.CREATED)
