from flask import request
from flask_restful import Resource
from main.services.auth import Auth

auth = Auth()


class Login(Resource):

    # TODO at login it must update variable last access
    @staticmethod
    def post():
        json = request.get_json()

        try:
            return auth.login(json), 201
        except Exception as error:
            return error, 409
