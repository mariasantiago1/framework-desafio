
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import traceback

from flask import Blueprint, Response

BLUEPRINT = Blueprint('logging', __name__)

handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=3)
logger = logging.getLogger('tdm')
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@BLUEPRINT.after_app_request
def log_response(response: Response):
    timestamp = strftime('[%d/%m/%Y %H:%M:%S]')
    logger.info(f"{timestamp} - {response.status} - {str(response.get_data())}")
    return response


def log_exception(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%d/%m/%Y %H:%M:%S]')
    logger.error(f"{timestamp} - ERROR {tb}")
    raise e