from main.repositories import UserRepository
from flask_jwt_extended import create_access_token
from main.extensions import db
from main.models import UserModel
from main.mappers import UserMapper


repository = UserRepository()
user_mapper = UserMapper()


class Auth:

    @staticmethod
    def login(data):
        entered_email = data['email']
        entered_password = data['password']

        user = db.session.query(UserModel).filter(UserModel.email == entered_email).first_or_404()

        if user.validate_password(entered_password):
            access_token = create_access_token(identity=user)
            data = {
                "user": user_mapper.dump(user),
                "token": access_token
            }
            return data
        else:
            return 'You have entered wrong credentials.', 401

    @staticmethod
    def logout(id):
        pass
