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
    @classmethod
    def _get_user(cls, email):
        """
        Gets the user specified by email or raises a 404 and aborts if a user
        is not found
        """
        try:
            return User.query.filter_by(email=email).one()
        except NoResultFound:
            abort(404, message="User {} doesn't exist.".format(email))

    @classmethod
    def _populate_user(cls, user):
        """
        Fills and saves the user object, with validation. Will add any fields
        that don't exist in the form submission from the model (patch).

        Returns True on success, dict of field errors on failure
        """
        form = UserForm()

        # Set defaults from model
        for field in form.data.keys():
            if field not in request.form:
                getattr(form, field).data = getattr(user, field)

        if form.validate_on_submit():
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()

            return True

        return form.errors

    @marshal_with(USER_FIELDS)
    def get(self, email):
        """
        List the user
        """
        return self._get_user(email)

    @marshal_with(USER_FIELDS)
    def post(self, email):
        """
        Edit an existing user
        """
        obj = self._get_user(email)
        result = self._populate_user(obj)

        if result is True:
            return obj, 201  # HTTP created
        else:
            return result, 400  # HTTP bad request

class UsersList(Resource):
    """
    Users list resource, used for creating a new user
    """
    @marshal_with(USER_FIELDS)
    def post(self):
        """
        Create a new user
        """
        obj = User()
        result = Users._populate_user(obj)

        if result is True:
            return obj, 201  # HTTP created
        else:
            return form.errors, 400  # HTTP bad request


api.add_resource(Users, '/users/<string:email>')
api.add_resource(UsersList, '/users/')