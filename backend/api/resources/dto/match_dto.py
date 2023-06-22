from flask_restx import Namespace, fields


matches_ns = Namespace("Matches", description="Operations related to matches")

create_match_request = matches_ns.model(
    "CreateMatchRequest",
    {
        "time": fields.String(required=True, description="Time when the match started"),
        "location": fields.String(
            required=False, description="Place where the match took place"
        ),
        "home_team_id": fields.Integer(
            required=True, description="Team ID of the home team"
        ),
        "guest_team_id": fields.Integer(
            required=True, description="Team ID of the guest team"
        ),
        "league_id": fields.Integer(required=False, description="League ID"),
        "guest_team_goals": fields.Integer(
            required=False, description="Number of goals scored by the guest team"
        ),
        "home_team_goals": fields.Integer(
            required=False, description="Number of goals scored by the home team"
        ),
    },
)
