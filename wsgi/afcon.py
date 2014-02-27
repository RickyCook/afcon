import flask
import os
import re

from flask import Flask, Response

app = Flask(__name__)
gear_uuid = getattr(os.environ, 'OPENSHIFT_GEAR_UUID', None)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/env')
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
    app.run()

