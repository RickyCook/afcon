from sqlalchemy_utils.types.password import PasswordType

from afcon import db


class User(db.Model):
    email = db.Column(db.String(254), primary_key=True)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']))

    nick_name = db.Column(db.String(100))
    real_name = db.Column(db.String(100))
    phone = db.Column(db.String(13))
