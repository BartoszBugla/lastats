from dataclasses import dataclass

from api.extensions import db

from .base import BaseModel


class Team(BaseModel):
    __tablename__ = "teams"

    name = db.Column(db.String(100), nullable=False, unique=True)
    league_points = db.Column(db.Integer, default=0)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"))
    players = db.relationship("Player", backref="teams", lazy=True)

    def __init__(self, name, league_points=0, league_id=None):
        self.name = name
        self.league_points = league_points
        self.league_id = league_id

    def __repr__(self):
        return f"<Team {self.name}>"
