from flask_restx import Namespace, Resource, marshal_with, fields
from flask import Response, request

from http import HTTPStatus

from api.extensions import db
from api.models.league import League


leagues_ns = Namespace("Leagues", description="Operations related to leagues")

MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "League not found"

team_model = leagues_ns.model(
    "team",
    {
        "id": fields.Integer(required=True, description="Team ID"),
        "name": fields.String(required=True, description="Team name"),
        "league_id": fields.Integer(required=True, description="League ID"),
        "league_name": fields.String(required=True, description="League name"),
    },
)

league_model = leagues_ns.model(
    "league",
    {
        "id": fields.Integer(required=True, description="League ID"),
        "name": fields.String(required=True, description="League name"),
        "teams": fields.List(
            fields.Nested(team_model),
            required=True,
            description="List of teams in the league",
        ),
    },
)


@leagues_ns.route("leagues")
@leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [league_model])
class ListAllTeams(Resource):
    @classmethod
    @marshal_with(league_model)
    def get(cls):
        """
        Returns list of all the leagues
        """
        return League.query.all()

    @classmethod
    @leagues_ns.response(HTTPStatus.CREATED, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @leagues_ns.response(HTTPStatus.CONFLICT, "CONFLICT")
    def post(cls):
        """
        Creates a new league.
        """
        data = request.json

        if not data:
            return {}, HTTPStatus.BAD_REQUEST

        league = League(data["name"])

        db.session.add(league)
        db.session.flush()
        db.session.commit()

        return {"id": id}, HTTPStatus.CREATED


@leagues_ns.route("leagues/<int:league_id>")
class Team(Resource):
    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @marshal_with(league_model)
    def get(cls, league_id):
        """
        Returns the league with the specified ID.
        """
        league: League = League.query.get_or_404(league_id)

        return league, 200

    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @leagues_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    def put(cls, team_id):
        """
        Updates league's data.
        """
        data = request.json

        if not data:
            return Response(status=HTTPStatus.BAD_REQUEST)

        league = League.query.filter_by(id=id)

        if league is None:
            return Response(status=HTTPStatus.NOT_FOUND)

        if data["name"]:
            league.update(data)
            db.session.commit()
            return Response(status=HTTPStatus.OK)

        return Response(status=HTTPStatus.NO_CONTENT)

    @classmethod
    def delete(cls, team_id):
        """
        Deletes the league with the specified ID.
        """
        league = League.query.filter_by(id=id)

        if league is None:
            return Response(status=HTTPStatus.NOT_FOUND)

        league.delete()

        db.session.commit()
        return Response(status=HTTPStatus.CREATED)
