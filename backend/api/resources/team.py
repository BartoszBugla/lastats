from flask_restx import Namespace, Resource
from flask import Response, abort, request

from http import HTTPStatus

teams_ns = Namespace("Teams", description="Operations related to teams")

MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "Team not found"

teams = {
       0: {"id": 0, "name": "Team Alpha"},
       1: {"id": 1, "name": "Team Bravo"},
       2: {"id": 2, "name": "Team Charlie"},
}

@teams_ns.route("teams")
@teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
class ListAllTeams(Resource):

    @classmethod
    def get(cls):
        """
        Returns list of all the teams whose names contain the given query.
        """
        return teams


@teams_ns.route("teams/<int:team_id>")
class Team(Resource):
    @classmethod
    @teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @teams_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
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

