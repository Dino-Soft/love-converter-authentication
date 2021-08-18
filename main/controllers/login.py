from flask import request
from flask_restful import Resource
from main.extensions import db
from main.services import AuthService
from main.models import UserModel

service = AuthService()


class Login(Resource):

    # TODO at login it must update variable last access
    @staticmethod
    def post():
        data = request.get_json()
        if data != '':
            try:
                return service.login(data), 200
            except Exception as e:
                return str(e), 401
