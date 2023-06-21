from dataclasses import dataclass

from api.extensions import db

from .base import BaseModel


class Team(BaseModel):
    __tablename__ = "teams"

    name = db.Column(db.String(100), nullable=False, unique=True)
    league_points = db.Column(db.Integer, default=0)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"))
    league = db.relationship("League", foreign_keys=[league_id], back_populates="teams")
    players = db.relationship("Player", backref="teams", lazy=True)
    wins = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

    def __init__(
        self, name, league_points=0, wins=0, draws=0, losses=0, league_id=None
    ):
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.name = name
        self.league_points = league_points
        self.league_id = league_id

    def __repr__(self):
        return f"<Team {self.name}>"
