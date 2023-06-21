from flask_restx import Resource

from sqlalchemy.orm import joinedload
from http import HTTPStatus


from api.models.match import Match

from .dto.match_dto import *
from .dto.base_models import *


MESSAGE_SUCCESS = "Operation completed successfully"


@matches_ns.route("matches")
class Matches(Resource):
    @classmethod
    @matches_ns.param("latest", "League ID")
    @matches_ns.response(HTTPStatus.OK, MESSAGE_SUCCESS, [match_model])
    @matches_ns.marshal_with(match_model)
    def get(cls):
        """
        Returns 10 first matches ordered descending by date
        """
        return (
            Match.query.order_by(Match.time.desc())
            .limit(10)
            .options(joinedload(Match.league))
            .all()
        )
