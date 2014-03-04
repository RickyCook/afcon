from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

from afcon import settings


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_CONNECTION

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)