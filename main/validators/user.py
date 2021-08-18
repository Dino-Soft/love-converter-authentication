from main.extensions import db
from main.models import UserModel
import re
from marshmallow import validate


regular_email = r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{1,15}$'
regular_password = r'^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{12,30}$'


def get_email_existance(email):
    try:
        email_exists = db.session.query(UserModel).filter(UserModel.email == email).scalar() is not None
        if email_exists:
            return 'The entered email address has already been registered', 409
    except validate.ValidationError as e:
        return e, 409


# TODO: HACER TEST PARA "check_email", "check_user" Y "check_password" METODOS..
def check_email(email):
    return re.match(regular_email, email) is not None if len(email) <= 100 else False


def check_user(username):
    return username.isalnum() if len(username) <= 100 else False


def check_password(password):
    return re.match(regular_password, password) is not None
