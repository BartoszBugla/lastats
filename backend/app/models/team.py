from dataclasses import dataclass

from app.extensions import db

from .base import BaseModel


@dataclass
class Team(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    league_points = db.Column(db.Integer, nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("league.id"), nullable=True)
    players = db.relationship("Player", backref="team", lazy=True)

    def __repr__(self):
        return f"<Team {self.name}>"
