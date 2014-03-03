from flask.ext.sqlalchemy import SQLAlchemy

from afcon.db import db


class User(db.Model):
    email = db.Column(db.String(254), primary_key=True)
    pw_hash = db.Column(db.LargeBinary())

    nick_name = db.Column(db.String(100))
    real_name = db.Column(db.String(100))
    phone = db.Column(db.String(13))
