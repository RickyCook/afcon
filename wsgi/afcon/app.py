import logging

from flask import Flask

from afcon import settings
from afcon.db import db


logging.basicConfig(**settings.LOGGING_CONFIG)
LOGGER = logging.getLogger()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_CONNECTION

db.init_app(app)

if settings.GEAR_UUID:
    logger.info('Running on OpenShift')


@app.route('/')
def hello():
    return "Hello World!"
