from flask_restx import Namespace, fields
from models.player import PlayerPosition


players_ns = Namespace("Players", description="Operations related to players")


create_player_request = players_ns.model(
    "CreatePlayerRequest",
    {
        "name": fields.String(required=True, description="Player name"),
        "position": fields.String(required=True, description="Player position", enum=PlayerPosition._member_names_),
        "team_id": fields.Integer(required=True, description="Player's team ID"),
    },
)
