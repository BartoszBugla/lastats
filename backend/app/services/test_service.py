from flask import abort
from random import random

from app.extensions import db
from app.models.test import Test


def create_test():
    new_test = Test(name="test")

    db.session.add(new_test)
    db.session.commit()

    return new_test.id


def get_all():
    tests = Test.query.all()
    results = []

    for test in tests:
        results.append(test)

    if random() > 0.5:
        raise abort(403)

    return results
