from flask_restx import Api
from api.resources.team import teams_ns

api = Api(
    title="Lastats API",
    version="1.0",
    description="API documentation for the backend of Lastats",
)
api.namespaces.clear()

api.add_namespace(teams_ns, path="/")
