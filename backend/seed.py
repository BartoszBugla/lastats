from datetime import datetime, timedelta
from api.extensions import db


from api.models.player import Player, PlayerPosition
from api.models.team import Team
from api.models.league import League
from api.models.match import Match
from api.models.match_event import MatchEvent, MatchEventType


def seed():
    seed_leagues()
    seed_teams()

    seed_matches()

    db.session.commit()


def seed_leagues():
    best_team = Team("Politechnika Śląska", 5, 5, 0, 2)
    best_team.players = [
        Player("Bartosz Bugla", 16, PlayerPosition.DEFENDER, 1),
        Player("Bartłomiej Pacia", 15, PlayerPosition.MIDFIELDER, 1),
        Player("Kamil Grabowski", 14, PlayerPosition.FORWARD, 1),
        Player("Michał Bober", 13, PlayerPosition.GOALKEEPER, 1),
    ]

    league = League(
        "Ekstraklasa",
    )

    league.teams = [
        Team("Legia Warszawa", 5, 5, 0, 2),
        Team("Piast Gliwice", 5, 2, 3, 4),
        Team(
            "Pogoń Szczecin",
            2,
            3,
            2,
            1,
        ),
        Team("Lech Poznań", 5, 2, 3, 4),
        Team("Podbiskdizie Bielska-Biała", 3, 2, 6, 4),
        Team("Wisła Kraków", 0, 5, 3, 4),
        Team("Śląsk Wrocław", 5, 5, 3, 4),
        Team("Ruch Chorzów", 3, 1, 6, 3),
        best_team,
    ]

    league2 = League("Testowa liga 2")
    db.session.add(league)
    db.session.add(league2)


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
        location="Warszawa",
        home_team_id=1,
        guest_team_id=2,
        league_id=1,
        guest_team_goals=1,
        home_team_goals=2,
    )

    match_item2 = Match(
        time=datetime.utcnow() - timedelta(days=1),
        location="Warszawa",
        home_team_id=4,
        guest_team_id=3,
        league_id=1,
        guest_team_goals=3,
        home_team_goals=2,
    )

    match_item.match_events = [
        MatchEvent(50, 1, MatchEventType.GOAL),
        MatchEvent(60, 1, MatchEventType.GOAL),
    ]

    db.session.add(match_item)
    db.session.add(match_item2)
