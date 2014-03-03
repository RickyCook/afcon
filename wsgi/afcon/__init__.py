import logging

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from afcon import settings


logging.basicConfig(**settings.LOGGING_CONFIG)
LOGGER = logging.getLogger()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_CONNECTION

db = SQLAlchemy(app)


if settings.GEAR_UUID:
    logger.info('Running on OpenShift')


@app.route('/')
def hello():
    return "Hello World!"
