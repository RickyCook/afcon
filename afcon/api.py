from flask import request
from flask.ext.restful import abort, fields, marshal_with, Resource
from sqlalchemy.orm.exc import NoResultFound

from afcon import api, db
from afcon.forms import UserForm
from afcon.models import User


USER_FIELDS = {
    'id': fields.Integer,
    'email': fields.String,
    'nick_name': fields.String,
    'real_name': fields.String,
    'phone': fields.String,
}

class Users(Resource):
    """
    User details resource, used for getting a specific user
    """
    def _get_user(self, email):
        try:
            return User.query.filter_by(email=email).one()
        except NoResultFound:
            abort(404, message="User {} doesn't exist.".format(email))

    @marshal_with(USER_FIELDS)
    def get(self, email):
        return self._get_user(email)


class UsersList(Resource):
    """
    Users list resource, used for creating a new user
    """
    @marshal_with(USER_FIELDS)
    def post(self):
        form = UserForm()
        
        if form.validate_on_submit():
            obj = User()
            form.populate_obj(obj)
            db.session.add(obj)
            db.session.commit()

            return obj, 201  # HTTP created

        return form.errors, 400  # HTTP bad request


api.add_resource(Users, '/users/<string:email>')
api.add_resource(UsersList, '/users/')