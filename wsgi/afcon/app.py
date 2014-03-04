import logging

from afcon import settings
from afcon.core import app


logging.basicConfig(**settings.LOGGING_CONFIG)
LOGGER = logging.getLogger()

if settings.GEAR_UUID:
    logger.info('Running on OpenShift')


@app.route('/')
def dragons():
    return "Here be dragons! (and an API)"
