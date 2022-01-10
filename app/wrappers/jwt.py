from functools import wraps
from werkzeug.exceptions import Unauthorized

from flask_jwt_extended import verify_jwt_in_request


def jwt_required(optional=False, fresh=False, refresh=False, locations=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(optional, fresh, refresh, locations)
                return fn(*args, **kwargs)
            except Exception as ex:
                raise Unauthorized(ex)

        return decorator

    return wrapper