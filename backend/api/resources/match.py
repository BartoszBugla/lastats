from flask import Response, request
from flask_restx import Resource
from datetime import datetime
from dateutil import parser

from sqlalchemy.orm import joinedload
from http import HTTPStatus

from api.extensions import db
from api.models.match import Match

from .dto.match_dto import *
from .dto.base_models import *


MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "Match not found"


@matches_ns.route("matches")
class Matches(Resource):
    @classmethod
    @matches_ns.param("latest", "League ID")
    @matches_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [match_model])
    @matches_ns.marshal_with(match_model)
    def get(cls):
        """
        Returns 10 first matches ordered descending by date
        """
        return (
            Match.query.order_by(Match.time.desc())
            .limit(10)
            .options(joinedload(Match.league))
            .all()
        )

    @classmethod
    @matches_ns.response(HTTPStatus.CREATED, MESSAGE_SUCCESS)
    @matches_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @matches_ns.response(HTTPStatus.CONFLICT, "CONFLICT")
    @matches_ns.expect(create_match_request)
    def post(cls):
        """
        Creates a new player.
        """
        data: dict = request.json

        new_match = Match(
            time=parser.parse(data["time"]),
            location=data["location"],
            home_team_id=data["home_team_id"],
            guest_team_id=data["guest_team_id"],
            league_id=data["league_id"],
        )
        db.session.add(new_match)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)


@matches_ns.route("matches/<int:match_id>")
class MatchById(Resource):
    @classmethod
    @matches_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, match_model)
    @matches_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @matches_ns.marshal_with(match_model)
    def get(cls, match_id):
        """
        Returns the match with the specified ID.
        """
        return Match.query.get(match_id)

    @classmethod
    @matches_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @matches_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @matches_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @matches_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    @matches_ns.expect(create_match_request)
    def put(cls, match_id):
        """
        Updates match data.
        """
        data = request.json

        match: Match = Match.query.get_or_404(match_id)

        match.name = data["name"] if "name" in data else match.name
        match.time = data["time"] if "time" in data else match.time
        match.location = data["location"] if "location" in data else match.location
        match.home_team_id = (
            data["home_team_id"] if "home_team_id" in data else match.home_team_id
        )
        match.guest_team_id = (
            data["guest_team_id"] if "guest_team_id" in data else match.guest_team_id
        )
        match.league_id = data["league_id"] if "league_id" in data else match.league_id
        match.guest_team_goals = (
            data["guest_team_goals"]
            if "guest_team_goals" in data
            else match.guest_team_goals
        )
        match.home_team_goals = (
            data["home_team_goals"]
            if "home_team_goals" in data
            else match.home_team_goals
        )

        db.session.commit()

        return "Match updated"

    @classmethod
    def delete(cls, match_id):
        """
        Deletes the match with the specified ID.
        """
        match: Match = Match.query.get_or_404(match_id)

        db.session.delete(match)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)
