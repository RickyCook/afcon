import logging

from flask import Flask

from afcon import settings

logging.basicConfig(**settings.LOGGING_CONFIG)
LOGGER = logging.getLogger()

app = Flask(__name__)

if settings.GEAR_UUID:
    logger.info('Running on OpenShift')

@app.route('/')
def hello():
    return "Hello World!"
