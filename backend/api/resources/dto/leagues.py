from flask_restx import Namespace, fields

from .teams import team_model

leagues_ns = Namespace("Leagues", description="Operations related to leagues")


league_model = leagues_ns.model(
    "LeagueModel",
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

create_league_request = leagues_ns.model(
    "CreateLeagueRequest",
    {"name": fields.String(required=True, description="League name")},
)


create_league_response = leagues_ns.model(
    "CreateLeagueResponse",
    {"id": fields.Integer(required=True, description="Created League ID")},
)

add_league_teams_request = leagues_ns.model(
    "AddLeagueTeamsRequest",
    {
        "ids": fields.List(
            fields.Integer, required=True, description="List of team IDs"
        ),
    },
)
