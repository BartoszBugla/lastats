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
            team_id=data["player_id"] if "player_id" in data else None,
        )
        db.session.add(new_player)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)


@players_ns.route("players/<int:player_id>")
class TeamById(Resource):
    @classmethod
    @players_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, player_model)
    @players_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @players_ns.marshal_with(player_model)
    def get(cls, player_id):
        """
        Returns the player with the specified ID.
        """
        return Player.query.get(player_id)

    @classmethod
    @players_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS)
    @players_ns.response(HTTPStatus.BAD_REQUEST, "BAD REQUEST")
    @players_ns.response(HTTPStatus.NOT_FOUND, MESSAGE_NOT_FOUND)
    @players_ns.response(HTTPStatus.NO_CONTENT, "NO_CONTENT")
    @players_ns.expect(create_player_request)
    def put(cls, player_id):
        """
        Updates player's data.
        """
        data = request.json

        player: Player = Player.query.get_or_404(player_id)

        player.name = data["name"] if "name" in data else player.name
        player.position = data["position"] if "position" in data else player.position
        player.team_id = data["team_id"] if "team_id" in data else player.team_id

        db.session.commit()

        return "Player updated"

    @classmethod
    def delete(cls, player_id):
        """
        Deletes the player with the specified ID.
        """
        player: Player = Player.query.get_or_404(player_id)

        db.session.delete(player)
        db.session.commit()

        return Response(status=HTTPStatus.CREATED)
