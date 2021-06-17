from werkzeug.security import check_password_hash, generate_password_hash

from main import db
from main.models import UserModel


class UserRepository:

    # Password security management
    @property
    def plain_password(self):
        raise AttributeError("The password can not be obtained. It is prohibited.")
        # We won't obtain the password accessing with a get method

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
        # We encrypt the plain text password from the JSON received in the user registration

    def validate_password(self, password):
        return check_password_hash(self.password, password)
        # Compares the received password with the database password

    @staticmethod
    def get_register_by_id(id):
        try:
            user = db.session.query(UserModel).get_or_404(id)
        except Exception as e:
            print(f"Exception: \n{e}")
        return user

    @staticmethod
    def delete_register_by_id(id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        try:
            db.session.commit()
        except Exception as e:
            print(f"Exception: \n{e}")
            db.session.rollback()
            return False
        return True

    @staticmethod
    def edit_register_by_id(id, data):
        user = db.session.query(UserModel).get_or_404(id)
        for key, values in data:
            setattr(user, key, values)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

    @staticmethod
    def create_register(email, data):
        email_exists = db.session.query(UserModel).filter(UserModel.email == email).scalar() is not None
        if email_exists:
            print(f"The entered email address has already been registered")
            return False
        else:
            # user = UserModel.from_json(request.get_json())
            db.session.add(data)
            db.session.commit()
            return True
