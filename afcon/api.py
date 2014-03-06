from flask.ext.restful import abort, fields, marshal_with, Resource
from sqlalchemy.orm.exc import NoResultFound

from afcon import api
from afcon.models import User


class Users(Resource):
    USER_FIELDS = {
        'email': fields.String,
        'nick_name': fields.String,
        'real_name': fields.String,
        'phone': fields.String,
    }

    def _get_user(self, email):
        try:
            return User.query.filter_by(email=email).one()
        except NoResultFound:
            abort(404, message="User {} doesn't exist.".format(email))

    @marshal_with(USER_FIELDS)
    def get(self, email):
        return self._get_user(email)


# class UsersList(Resource):
#     def get(self):
#         return []


api.add_resource(Users, '/users/<string:email>')
# api.add_resource(UserList, '/users/')