import enum

from app.extensions import db

from .base import BaseModel


class MatchEventType(enum.Enum):
    RED_CARD = 1
    YELLOW_CARD = 2
    FAUL = 3
    GOAL = 4


class MatchEvent(BaseModel):
    __tablename__ = "match_events"

    match_minute = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    type = db.Column(db.Enum(MatchEventType), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"))

    def __init__(self, match_minute, player_id, type):
        self.match_minute = match_minute
        self.player_id = player_id
        self.type = type

    def __repr__(self):
        return f"<Player {self.name}>"
