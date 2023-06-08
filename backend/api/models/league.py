from api.extensions import db

from .base import BaseModel


class League(BaseModel):
    __tablename__ = "leagues"

    name = db.Column(db.String(100), nullable=False, unique=True)

    Teams = db.relationship("Team", backref="leagues", lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<League {self.name}>"
