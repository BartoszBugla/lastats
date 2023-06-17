from flask import Blueprint, jsonify

errors_bp = Blueprint("errors", __name__)


@errors_bp.get("/")
def index():
    return "Welcome to Lacrosse API"


def error_response(message: str, code: int, details: str = None):
    return jsonify({"message": message, "code": code, "details": details}), code


@errors_bp.app_errorhandler(Exception)
def internal_server_error(e: Exception):
    return error_response(
        "INTERNAL_ERROR",
        500,
        f"{type(e).__name__}: {e.__str__()}",
    )


@errors_bp.app_errorhandler(404)
def page_not_found(e: Exception):
    return error_response("NOT FOUND", 404, e.__str__())


@errors_bp.app_errorhandler(403)
def page_not_found(e: Exception):
    return error_response("FORBIDDEN", 403, e.__str__())
