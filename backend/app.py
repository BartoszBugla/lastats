import logging

from flask import Flask
from flask_cors import CORS, cross_origin


from api.extensions import db
from api.api_extension import api

from config import get_env_config
from seed import seed


def create_app():
    app = Flask(__name__)

    # load config
    app.config.from_object(get_env_config())
    print(f"app config: {app.config}")

    # extensions
    db.init_app(app)
    api.init_app(app)
    # migrate.init_app(app, db)
    CORS(app)

    # set logger
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.ERROR)

    @app.route("/swagger.json")
    def spec():
        return api.as_json()

    with app.app_context():
        print("Dropping all tables and creating new ones...")
        db.drop_all()
        db.create_all()
        seed()

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"],
    )
