from flask_restx import Namespace, fields

teams_ns = Namespace("Teams", description="Operations related to teams")

team_model = teams_ns.model(
    "TeamModel",
    {
        "id": fields.Integer(required=True, description="Team ID"),
        "name": fields.String(required=True, description="Team name"),
        "league_id": fields.Integer(required=True, description="League ID"),
        "league_name": fields.String(required=True, description="League name"),
    },
)

create_team_request = teams_ns.model(
    "CreateTeamRequest",
    {
        "name": fields.String(required=True, description="Team name"),
    },
)
