from flask import Flask
from flask_cors import CORS, cross_origin

import logging

from app.extensions import db

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
    from app.controllers.test_controller import test_bp
    from app.controllers.errors import errors_bp

    app.register_blueprint(test_bp, url_prefix="/test")
    app.register_blueprint(errors_bp, url_prefix="/")

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()
        seed()

    app.run(port=app.config["PORT"], debug=True)
