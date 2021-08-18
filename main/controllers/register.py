from flask import request
from flask_restful import Resource

from main.services import UserService

service = UserService()


class Register(Resource):

    @staticmethod
    def post():
        json = request.get_json()
        try:
            service.add_user(json)
            return 'Done. Please activate your account in order to sign in', 201
        except Exception as error:
            return error, 409
