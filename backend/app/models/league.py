from app.extensions import db

from .base import BaseModel


class League(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    Teams = db.relationship("Team", backref="league", lazy=True)

    def __repr__(self):
        return f"<League {self.name}>"
