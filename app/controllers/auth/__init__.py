from flask import Blueprint, jsonify, request
from werkzeug.exceptions import Unauthorized

from flask_jwt_extended import JWTManager, create_access_token

from app.repositories import user

BLUEPRINT = Blueprint('auth', __name__)

jwt = JWTManager()


@BLUEPRINT.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    if user.authenticate(username, password) is None:
        raise Unauthorized("Invalid username or password")

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)