import os


class BaseConfig(object):
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = True

    def __init__(self):
        print('CREATED!!!')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    def __init__(self):
        print('CREATED!!!')

    DEBUG = True
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(PROJECT_PATH, "database.db")


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "TODO"


def get_env_config() -> str:
    flask_config_name = os.getenv("FLASK_ENVIRONMENT_CONFIG", "dev")
    envs = ["prod", "dev"]
    if flask_config_name not in envs:
        raise ValueError(
            f"The environment config value must be one of these values: {envs}"
        )
    print(f'mapper: {CONFIGURATION_MAPPER[flask_config_name]}')
    return CONFIGURATION_MAPPER[flask_config_name]


CONFIGURATION_MAPPER = {
    "dev": "config.DevelopmentConfig",
    "prod": "config.ProductionConfig",
}
