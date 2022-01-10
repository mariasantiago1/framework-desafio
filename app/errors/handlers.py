from werkzeug.exceptions import NotFound, InternalServerError
from . import BLUEPRINT


@BLUEPRINT.app_errorhandler(NotFound)
def not_found(_):
    """Page not found."""
    return make_response('Resource not found', 404)


@BLUEPRINT.app_errorhandler(InternalServerError)
def internal_error(_):
    return 'An internal error has occurred', 500
