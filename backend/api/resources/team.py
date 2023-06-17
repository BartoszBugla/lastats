from flask_restx import Namespace, Resource

from http import HTTPStatus

teams_ns = Namespace("Teams", description="Operations related to teams")

MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "Team not found"

@teams_ns.route("teams")
@teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
class ListAllTeams(Resource):

    @classmethod
    def get(cls):
        """
        Returns list of all the teams whose names contain the given query.
        """


@teams_ns.route("teams/<int:id>")
@teams_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
@teams_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
class Team(Resource):
    @classmethod
    def get(cls):
        pass

    @classmethod
    def post(cls):
        pass

    @classmethod
    def delete(cls):
        pass

