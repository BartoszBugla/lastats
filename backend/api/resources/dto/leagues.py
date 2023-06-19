from flask_restx import Namespace, fields

from .teams import team_model

leagues_ns = Namespace("Leagues", description="Operations related to leagues")


league_model = leagues_ns.model(
    "league",
    {
        "id": fields.Integer(required=True, description="League ID"),
        "name": fields.String(required=True, description="League name"),
        "teams": fields.List(
            fields.Nested(team_model),
            required=True,
            description="List of teams in the league",
        ),
    },
)
