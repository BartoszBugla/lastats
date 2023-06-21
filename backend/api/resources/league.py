from flask_restx import Namespace, Resource, marshal_with, fields
from flask import Response, request, abort

from http import HTTPStatus
from dateutil import parser

from api.extensions import db
from api.models.league import League
from api.models.team import Team
from api.models.match import Match

from .dto.league_dto import *
from .dto.base_models import *


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
    @leagues_ns.expect(create_league_request, validate=True)
    def post(cls):
        """
        Creates a new league.
        """
        data = request.json

        if not data:
            return abort(HTTPStatus.BAD_REQUEST)

        league: League = League(data["name"])

        db.session.add(league)
        db.session.flush()
        db.session.commit()

        return {"id": league.id}


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

        return league

    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, create_league_response)
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @leagues_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    @leagues_ns.expect(create_league_request, validate=True)
    def put(cls, league_id):
        """
        Updates league's data.
        """
        data = request.json

        league: League = League.query.get_or_404(league_id)

        league.name = data["name"]

        db.session.commit()

        return "League updated"

    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    def delete(cls, league_id):
        """
        Deletes the league with the specified ID.
        """
        league: League = League.query.get_or_404(league_id)

        db.session.delete(league)
        db.session.commit()

        return "League deleted"


@leagues_ns.route("leagues/<int:league_id>/teams")
class LeagueTeams(Resource):
    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @leagues_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD_REQUEST")
    @leagues_ns.expect(add_league_teams_request, validate=True)
    def post(cls, league_id):
        """
        Appends teams with the specified IDs to the league.
        """

        data = request.json

        teams: list[Team] = Team.query.filter(Team.id.in_(data["ids"])).all()

        for team in teams:
            team.league_id = league_id

        db.session.commit()

        return "Teams added to league"


@leagues_ns.route("leagues/<int:league_id>/matches")
class LeagueMathes(Resource):
    @classmethod
    @leagues_ns.response(HTTPStatus.OK, "Match Added to league")
    @leagues_ns.response(HTTPStatus.BAD_REQUEST, "BAD_REQUEST")
    @leagues_ns.expect(add_match_to_league_request, validate=True)
    def post(cls, league_id):
        """
        Create match withing the league.
        """
        data = request.json

        new_match = Match(
            parser.parse(data["time"]),
            data["location"],
            data["home_team_id"],
            data["guest_team_id"],
            league_id,
        )

        db.session.add(new_match)
        db.session.commit()

        return "Match Added to league"

    @classmethod
    @leagues_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [match_model])
    @marshal_with(match_model)
    def get(cls, league_id):
        matches: list[Match] = Match.query.filter(Match.league_id == league_id).all()
        return matches
