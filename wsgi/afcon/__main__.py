import flask
import re

from flask import Response

from afcon import routes
from afcon.core import app, manager
from afcon.settings import GEAR_UUID

def env():
    exclude_re = r'OPENSHIFT|PASSWORD|^PG'

    lines = [
        "{} => {}".format(key, value)
        for key, value
        in flask.request.environ.items()
        if not (
            re.search(exclude_re, key) or
            (GEAR_UUID and re.search(
                GEAR_UUID, value
            ))
        )
    ]

    return Response(
        "\n".join(lines),
        content_type='text/plain;charset=UTF-8'
    )

app.route('/env')(env)

manager.run()