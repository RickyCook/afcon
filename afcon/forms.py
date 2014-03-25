import re

from flask.ext.wtf import Form

from wtforms import validators
from wtforms.ext.sqlalchemy.orm import converts, ModelConverter, model_form

from afcon.models import User


class AUPhoneValidator(validators.Regexp):
    """
    Simple validator for AU phone numbers
    """
    REGEX = re.compile(r'^[0-9]{10}$')
    def __init__(self, *args, **kwargs):
        super(AUPhoneValidator, self).__init__(self.REGEX, *args, **kwargs)


class UserFormConverter(ModelConverter):
    """
    Convert remaining UserForm fields that can't be automagically converted
    """
    @converts('PasswordType')
    def conv_password(self, *args, **kwargs):
        return self.conv_String(*args, **kwargs)


UserForm = model_form(User, base_class=Form, field_args={
    'email': {'validators': [validators.DataRequired(), validators.Email()]},
    'password': {'validators': [validators.DataRequired()]},
    'nick_name': {'validators': [validators.DataRequired()]},
    'real_name': {'validators': [validators.DataRequired()]},
    'phone': {'validators': [validators.DataRequired(), AUPhoneValidator()]},
}, converter=UserFormConverter())