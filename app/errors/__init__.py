from flask import Blueprint, make_response
from werkzeug.exceptions import NotFound, InternalServerError, MethodNotAllowed, BadRequest, Unauthorized

import app.logging as logging

BLUEPRINT = Blueprint('errors', __name__)


@BLUEPRINT.app_errorhandler(Unauthorized)
def unauthorized(msg):
    error = {'error': {'reason': str(msg)}}
    
    return make_response(error, 401)


@BLUEPRINT.app_errorhandler(NotFound)
def not_found(_):
    error = {'error': {'reason': 'Resource not found'}}
    
    return make_response(error, 404)


@BLUEPRINT.app_errorhandler(MethodNotAllowed)
def method_not_allowed(_):
    error = {'error': {'reason': 'The method is not allowed for the requested URL'}}
    
    return make_response(error, 405)


@BLUEPRINT.app_errorhandler(InternalServerError)
def internal_error(_):
    error = {'error': {'reason': 'An internal error has occurred'}}
    
    return make_response(error, 500)


@BLUEPRINT.app_errorhandler(Exception)
def exceptions(e):
    logging.exception(e)