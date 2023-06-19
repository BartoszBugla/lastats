from flask_restx import Namespace, Resource, marshal_with, fields

teams_ns = Namespace("Teams", description="Operations related to teams")

team_model = teams_ns.model(
    "team",
    {
        "id": fields.Integer(required=True, description="Team ID"),
        "name": fields.String(required=True, description="Team name"),
        "league_id": fields.Integer(required=True, description="League ID"),
        "league_name": fields.String(required=True, description="League name"),
    },
)
