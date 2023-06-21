from flask_restx import Namespace, fields


teams_ns = Namespace("Teams", description="Operations related to teams")


create_team_request = teams_ns.model(
    "CreateTeamRequest",
    {
        "name": fields.String(required=True, description="Team name"),
        "goals": fields.Integer(required=False, description="Number of goals"),
        "draws": fields.Integer(required=False, description="Number of draws"),
        "losses": fields.Integer(required=False, description="Number of losses"),
        "league_points": fields.Integer(required=False, description="Number of points"),
        "league_id": fields.Integer(required=False, description="League ID"),
    },
)

# from .league import league_model

# team_model["league"] = fields.Nested(league_model)
