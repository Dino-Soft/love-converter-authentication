from flask import request
from flask_restful import Resource

from main.services import UserService

service = UserService()


class Register(Resource):

    # TODO Hacer manejo de errores ante json vacios que ingresan
    @staticmethod
    def post():
        data = request.get_json()
        try:
            service.add_user(data)
            return 'Done. Please activate your account in order to sign in', 201
        except Exception as error:
            return error, 409
