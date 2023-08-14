from flask import render_template

# noinspection PyProtectedMember
from flask_wtf.csrf import CSRFError
from werkzeug.exceptions import Forbidden, NotFound

from blueprints.errors import errors_bp


# noinspection PyUnusedLocal
@errors_bp.app_errorhandler(401)
def unauthorized_error(error):
    # noinspection PyUnresolvedReferences
    return render_template("errors/401.html"), 401


# noinspection PyUnusedLocal
@errors_bp.app_errorhandler(403)
@errors_bp.app_errorhandler(Forbidden)
def forbidden_error(error):
    # noinspection PyUnresolvedReferences
    return render_template("errors/403.html"), 403


# noinspection PyUnusedLocal
@errors_bp.app_errorhandler(404)
@errors_bp.app_errorhandler(NotFound)
def not_found_error(error):
    # noinspection PyUnresolvedReferences
    return render_template("errors/404.html"), 404


@errors_bp.app_errorhandler(CSRFError)
def csrf_error(error):
    # noinspection PyUnresolvedReferences
    return render_template("errors/csrf_error.html", reason=error.description), 400
