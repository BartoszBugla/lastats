import enum

from app.extensions import db

from .base import BaseModel


class PlayerPosition(enum.Enum):
    GOALKEEPER = 1
    DEFENDER = 2
    MIDFIELDER = 3
    FORWARD = 4


class Player(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Enum(PlayerPosition))
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    def __repr__(self):
        return f"<Player {self.name}>"
