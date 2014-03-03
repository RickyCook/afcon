import flask
import logging
import os
import re

from flask import Flask, Response

from afcon import settings

logging.basicConfig(**settings.LOGGING_CONFIG)
LOGGER = logging.getLogger()

app = Flask(__name__)

if settings.GEAR_UUID:
    logger.info('Running on OpenShift')

@app.route("/")
def hello():
    return "Hello World!"

def env():
    exclude_re = r'OPENSHIFT|PASSWORD|^PG'

    lines = [
        "{} => {}".format(key, value)
        for key, value
        in flask.request.environ.items()
        if not (
            re.search(exclude_re, key) or
            (settings.GEAR_UUID and re.search(
                settings.GEAR_UUID, value
            ))
        )
    ]

    return Response(
        "\n".join(lines),
        content_type="text/plain;charset=UTF-8"
    )

if __name__ == "__main__":
    app.route('/env')(env)
    app.run()

