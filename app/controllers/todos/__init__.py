from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

from .utils import _fetch_todos
from app.wrappers.jwt import jwt_required

BLUEPRINT = Blueprint('todos', __name__)


@BLUEPRINT.route('/', methods=['GET'])
@jwt_required()
def get_todos():
    todos = _fetch_todos()

    if todos is None:
        raise NotFound

    return jsonify(todos)