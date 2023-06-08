import logging

from flask import Flask
from flask_cors import CORS, cross_origin

from api.extensions import db

from config import DevelopmentConfig
from seed import seed


def create_app():
    """Create Flask app."""
    app = Flask(__name__)

    # load config
    app.config.from_object(DevelopmentConfig())

    # extensions
    db.init_app(app)
    # migrate.init_app(app, db)
    CORS(app)

    # set logger
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.ERROR)

    # register blueprints
    from api.controllers.errors import errors_bp
    from api.controllers.leagues_controller import league_bp

    app.register_blueprint(errors_bp, url_prefix="/")
    app.register_blueprint(league_bp, url_prefix="/leagues")

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()
        seed()

    app.run(port=app.config["PORT"], debug=True)
