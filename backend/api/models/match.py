import enum

from api.extensions import db

from .base import BaseModel


class Match(BaseModel):
    __tablename__ = "matches"

    time = db.Column(db.DateTime(), nullable=False)
    location = db.Column(db.String(100))
    host_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    guest_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"))

    match_events = db.relationship("MatchEvent", backref="matches", lazy=True)

    def __init__(self, time, location, host_team_id, guest_team_id, league_id):
        self.time = time
        self.location = location
        self.host_team_id = host_team_id
        self.guest_team_id = guest_team_id
        self.league_id = league_id

    def __repr__(self):
        return f"<Player {self.name}>"
