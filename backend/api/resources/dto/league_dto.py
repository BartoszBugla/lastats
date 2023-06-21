from flask_restx import Namespace, fields


leagues_ns = Namespace("Leagues", description="Operations related to leagues")


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

add_match_to_league_request = leagues_ns.model(
    "AddMatchToLeagueRequest",
    {
        "home_team_id": fields.Integer(
            required=True, description="Home team ID", nullable=False
        ),
        "guest_team_id": fields.Integer(required=True, description="Guest team ID"),
        "time": fields.DateTime(required=True, description="Match time"),
        "location": fields.String(required=True, description="Match location"),
    },
)
