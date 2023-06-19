from flask_restx import Namespace, Resource, marshal_with, fields
from flask import Response, request

from http import HTTPStatus

from api.extensions import db
from api.models.league import League

from .dto.leagues import *


MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "League not found"


@leagues_ns.route("leagues")
class Leagues(Resource):
    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [league_model])
    @leagues_ns.marshal_with(league_model)
    def get(cls):
        """
        Returns list of all the leagues
        """
        return League.query.all()

    @classmethod
    @leagues_ns.response(HTTPStatus.CREATED, MESSAGE_SUCCESS, create_league_response)
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @leagues_ns.response(HTTPStatus.CONFLICT, "CONFLICT")
    @leagues_ns.expect(create_league_request)
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
class LeagueById(Resource):
    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, league_model)
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @leagues_ns.marshal_with(league_model)
    def get(cls, league_id):
        """
        Returns the league with the specified ID.
        """
        league: League = League.query.get_or_404(league_id)

        return league, 200

    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, create_league_response)
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @leagues_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    @leagues_ns.expect(create_league_request)
    def put(cls):
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
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    def delete(cls, league_id):
        """
        Deletes the league with the specified ID.
        """
        league = League.query.filter_by(id=league_id)

        if league is None:
            return Response(status=HTTPStatus.NOT_FOUND)

        league.delete()

        db.session.commit()
        return Response(status=HTTPStatus.OK)


@leagues_ns.route("leagues/<int:league_id>/teams")
class LeagueTeams(Resource):
    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @leagues_ns.expect(add_league_teams_request)
    def post(cls, league_id):
        """
        Appends teams with the specified IDs to the league.
        """
        league = League.query.filter_by(id=league_id)

        if league is None:
            return Response(status=HTTPStatus.NOT_FOUND)

        league.delete()

        db.session.commit()
        return Response(status=HTTPStatus.OK)
