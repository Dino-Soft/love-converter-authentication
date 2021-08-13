from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from main.extensions import db
from main.mappers import UserMapper
from main.models import UserModel
from main.validators import check_email, check_password

user_mapper = UserMapper()


class Login(Resource):

    # TODO at login it must update variable last access
    @staticmethod
    def post():
        data = request.get_json()
        entered_email = data['email']
        entered_password = data['password']

        user = db.session.query(UserModel).filter(UserModel.email == entered_email).first_or_404()

        if user.validate_password(entered_password):
            access_token = create_access_token(identity=user)
            data = {
                "user": user_mapper.dump(user),
                "token": access_token
            }
            return data, 200
        else:
            return 'You have entered wrong credentials.', 401
