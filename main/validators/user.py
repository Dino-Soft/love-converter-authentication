from main.extensions import db
from main.models import UserModel
import re
from marshmallow import validate

check_email = r"/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i"


def get_email_existance(email):
    try:
        email_exists = db.session.query(UserModel).filter(UserModel.email == email).scalar() is not None
        if email_exists:
            return 'The entered email address has already been registered', 409
    except validate.ValidationError as e:
        return e, 409


def checking_email(email):
    return re.match(check_email, email) is not None
