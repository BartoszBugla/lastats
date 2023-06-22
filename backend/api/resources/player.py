from flask_restx import Resource
from flask import Response, request

from http import HTTPStatus

from api.extensions import db
from api.models.player import Player

from .dto.player_dto import *
from .dto.base_models import *

MESSAGE_SUCCESS = "Operation completed successfully"
MESSAGE_NOT_FOUND = "Player not found"


@players_ns.route("players")
class Players(Resource):
    @classmethod
    @players_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [player_model])
    @players_ns.marshal_list_with(player_model)
    def get(cls):
        """
        Returns list of all the players whose names contain the given query.
        """
        return Player.query.all()

    @classmethod
    @players_ns.response(HTTPStatus.CREATED, MESSAGE_SUCCESS)
    @players_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @players_ns.response(HTTPStatus.CONFLICT, "CONFLICT")
    @players_ns.expect(create_player_request)
    def post(cls):
        """
        Creates a new player.
        """
        data: dict = request.json

        new_player = Player(
            name=data["name"],
            position=data["position"],
            team_id=data["team_id"] if "team_id" in data else None,
        )
        db.session.add(new_player)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)
