from flask_jwt_extended import create_access_token

from main.repositories import UserRepository
from main.mappers import UserMapper

mapper = UserMapper()
repository = UserRepository()
user_mapper = UserMapper()


class Auth:

    @staticmethod
    def login(data):
        entered_password = data['password']

        user = repository.get_user_by_email(data['email'])

        if user.validate_password(entered_password):
            access_token = create_access_token(identity=user)
            user_data = {
                "user": mapper.dump(user),
                "token": access_token
            }
            return user_data
        else:
            raise Exception('You have entered wrong credentials.')
