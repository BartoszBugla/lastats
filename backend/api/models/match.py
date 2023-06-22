from api.extensions import db

from .base import BaseModel


class Match(BaseModel):
    __tablename__ = "matches"

    time = db.Column(db.DateTime(), nullable=False)
    location = db.Column(db.String(100))
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    guest_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    home_team = db.relationship("Team", foreign_keys=[home_team_id])
    guest_team = db.relationship("Team", foreign_keys=[guest_team_id])
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"))
    league = db.relationship("League", foreign_keys=[league_id])
    guest_team_goals = db.Column(db.Integer, default=0)
    home_team_goals = db.Column(db.Integer, default=0)
    match_events = db.relationship("MatchEvent", backref="matches", lazy=True)

    def __init__(
        self,
        time,
        location,
        home_team_id,
        guest_team_id,
        league_id,
        guest_team_goals,
        home_team_goals,
    ):
        self.time = time
        self.location = location
        self.home_team_id = home_team_id
        self.guest_team_id = guest_team_id
        self.league_id = league_id
        self.guest_team_goals = guest_team_goals
        self.home_team_goals = home_team_goals

    def __repr__(self):
        return f"<Player {self.name}>"
