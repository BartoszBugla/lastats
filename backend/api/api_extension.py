from flask_restx import Api

from api.resources.team import teams_ns
from api.resources.league import leagues_ns
from api.resources.match import matches_ns
from api.resources.dto.base_models import base_ns

api = Api(
    title="Lastats API",
    version="1.0",
    description="API documentation for the backend of Lastats",
)

api.namespaces.clear()

api.add_namespace(base_ns, path="/")
api.add_namespace(teams_ns, path="/")
api.add_namespace(leagues_ns, path="/")
api.add_namespace(matches_ns, path="/")
