from app.extensions import db

from app.models.test import Test
from app.models.player import Player, PlayerPosition
from app.models.team import Team
from app.models.league import League


def seed():
    db.session.add(Test(name="test"))
    db.session.add(Test(name="test2"))
    db.session.add(Test(name="test3"))
    db.session.add(Test(name="test4"))

    db.session.add(
        Player(
            name="testowy player",
            position=PlayerPosition.DEFENDER,
        )
    )

    db.session.add(
        Team(
            name="Testowa druzyna",
            league_points=0,
        )
    )

    db.session.add(League(name="Testowa liga"))

    db.session.commit()

    pass
