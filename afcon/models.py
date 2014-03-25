from sqlalchemy_utils.types.password import PasswordType

from afcon import db


class User(db.Model):
    """
    Basic user model
    """
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(254), nullable=False)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']))

    nick_name = db.Column(db.String(100), nullable=False)
    real_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
