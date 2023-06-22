from flask_restx import Namespace, fields, Model

base_ns = Namespace("Base models for lastats API")


base_model: Model = base_ns.model(
    "BaseModel",
    {
        "id": fields.Integer(required=True, description="ID"),
        "updated_at": fields.DateTime(required=True, description="Updated at"),
        "created_at": fields.DateTime(required=True, description="Created at"),
    },
)


team_model = base_ns.inherit(
    "TeamModel",
    base_model,
    {
        "name": fields.String(required=True, description="Team name"),
        "league_id": fields.Integer(required=True, description="League ID"),
        "wins": fields.Integer(required=True, description="Number of wins"),
        "draws": fields.Integer(required=True, description="Number of draws"),
        "losses": fields.Integer(required=True, description="Number of losses"),
        "league_points": fields.Integer(required=True, description="League points"),
    },
)

league_model = base_ns.inherit(
    "LeagueModel",
    base_model,
    {
        "name": fields.String(required=True, description="League name"),
        "teams": fields.List(
            fields.Nested(team_model),
            required=True,
            description="List of teams in the league",
        ),
    },
)


match_event_model = base_ns.inherit(
    "MatchEventModel",
    base_model,
    {
        "match_id": fields.Integer(required=True, description="Match ID"),
        "match_minute": fields.Integer(required=True, description="Match minute"),
        "player_id": fields.Integer(required=True, description="Player ID"),
        "type": fields.String(required=True, description="Match event type"),
    },
)


match_model = base_ns.inherit(
    "MatchModel",
    base_model,
    {
        "home_team_id": fields.Integer(required=True, description="Home team ID"),
        "guest_team_id": fields.Integer(required=True, description="Guest team ID"),
        "home_team": fields.Nested(team_model),
        "guest_team": fields.Nested(team_model),
        "home_team_goals": fields.Integer(required=True, description="Home team goals"),
        "guest_team_goals": fields.Integer(
            required=True, description="Guest team goals"
        ),
        "league_id": fields.Integer(required=True, description="League ID"),
        "league": fields.Nested(league_model),
        "match_events": fields.List(fields.Nested(match_event_model)),
        "location": fields.String(required=True, description="Match location"),
        "time": fields.DateTime(required=True, description="Match event time"),
    },
)

player_model = base_model.inherit(
    "PlayerModel",
    base_model,
    {
        "name": fields.String(required=True, description="Player name"),
        "position": fields.String(required=True, description="Player position"),
        "team_id": fields.Integer(required=True, description="Player team ID"),
    },
)
