import logging

from flask import Flask
from flask_cors import CORS, cross_origin

from api.extensions import db

from config import get_env_config
from seed import seed


def create_app():
    app = Flask(__name__)

    # load config
    app.config.from_object(get_env_config())
    print(f'app config: {app.config}')

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
    from api.controllers.teams_controller import teams_bp

    app.register_blueprint(errors_bp, url_prefix="/")
    app.register_blueprint(league_bp, url_prefix="/leagues")
    app.register_blueprint(teams_bp, url_prefix="/teams")

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()
        seed()

    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"],
    )
