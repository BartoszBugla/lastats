from app.extensions import db
from app.models.test import Test


def seed():
    db.session.add(Test(name="test"))
    db.session.add(Test(name="test2"))
    db.session.add(Test(name="test3"))
    db.session.add(Test(name="test4"))

    db.session.commit()
