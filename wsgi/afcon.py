import flask
import logging
import os
import re

from flask import Flask, Response

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
LOGGER = logging.getLogger()

app = Flask(__name__)
gear_uuid = getattr(os.environ, 'OPENSHIFT_GEAR_UUID', None)

if gear_uuid:
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
            (gear_uuid and re.search(gear_uuid, value))
        )
    ]

    return Response(
        "\n".join(lines),
        content_type="text/plain;charset=UTF-8"
    )

if __name__ == "__main__":
    app.route('/env')(env)
    app.run()

