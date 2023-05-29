import os


class DevelopmentConfig(object):
    """Base config class."""

    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

    PORT = 8000

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(PROJECT_PATH, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False