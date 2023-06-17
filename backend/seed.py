from datetime import datetime
from api.extensions import db


from api.models.player import Player, PlayerPosition
from api.models.team import Team
from api.models.league import League
from api.models.match import Match
from api.models.match_event import MatchEvent, MatchEventType


def seed():
    seed_leagues()
    seed_teams()
    seed_players()
    seed_matches()

    db.session.commit()


def seed_leagues():
    league = League("Testowa liga")
    league2 = League("Testowa liga 2")
    db.session.add(league)
    db.session.add(league2)


def seed_players():
    player = Player(name="Testowy gracz", position=PlayerPosition.DEFENDER, team_id=1)
    db.session.add(player)


def seed_teams():
    team = Team("Testowy zesp 12", 5, 2)
    team2 = Team("Testowy zesp 2", 3, 2)
    team3 = Team("Testowy zesp 3", 3, 2)
    team4 = Team("Testowy zesp 4", 3, 2)

    db.session.add(team)
    db.session.add(team2)
    db.session.add(team3)
    db.session.add(team4)


def seed_matches():
    match_item = Match(
        time=datetime.utcnow(),
        location="test",
        host_team_id=1,
        guest_team_id=2,
        league_id=1,
    )

    match_item.match_events = [
        MatchEvent(50, 1, MatchEventType.GOAL),
        MatchEvent(60, 1, MatchEventType.GOAL),
    ]

    db.session.add(match_item)
