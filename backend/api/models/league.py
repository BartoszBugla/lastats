from api.extensions import db

from .base import BaseModel

from dataclasses import dataclass


@dataclass
class League(BaseModel):
    __tablename__ = "leagues"

    name = db.Column(db.String(100), nullable=False, unique=True)

    teams = db.relationship("Team", back_populates="league", lazy=True)
    matches = db.relationship("Match", back_populates="league", lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<League {self.name}>"
