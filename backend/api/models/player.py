import enum

from api.extensions import db

from .base import BaseModel


class PlayerPosition(enum.Enum):
    GOALKEEPER = 1
    DEFENDER = 2
    MIDFIELDER = 3
    FORWARD = 4


class Player(BaseModel):
    __tablename__ = "players"

    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Enum(PlayerPosition))
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))

    def __init__(self, name, position=None, team_id=None):
        self.name = name
        self.position = position
        self.team_id = team_id

    def __repr__(self):
        return f"<Player {self.name}>"
