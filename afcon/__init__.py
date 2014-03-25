import os

from flask import Flask
from flask.ext.migrate import Migrate
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = os.environ.get('OPENSHIFT_SECRET_TOKEN',
                                'THIS IS REALLY SECRET')
app.config['WTF_CSRF_ENABLED'] = False  # Bad for API
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL',
                   'sqlite:///{}'.format(os.path.abspath('../afcon.db'))
                   )

try:
    app.static_folder = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi')
except KeyError:
    pass

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import afcon.views
import afcon.api