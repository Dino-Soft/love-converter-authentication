from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from main.extensions import db
from main.mappers import UserMapper
from main.models import UserModel
from main.validators import check_email, check_password

user_mapper = UserMapper()


class Login(Resource):

    @staticmethod
    def post():
        entered_email = str(request.get_json().get('email'))
        entered_password = str(request.get_json().get('password'))

        # TODO Esta logica deberia estar en el servicio, el controlador solo deberia obtener el json y pasarselo al servicio


        # TODO Deshabilitado porque trae problemas -->> Corregir.
        # if check_email(entered_email) and check_password(entered_password):
        user = db.session.query(UserModel).filter(UserModel.email == entered_email).first_or_404()
        
        # TODO validate_password es un metodo del "user" antes declarado?
        # True value if both passwords match
        if user.validate_password(entered_password):
            access_token = create_access_token(identity=user)
            data = {
                "user": user_mapper.dump(user),
                "token": access_token
            }
            return data, 200
        else:
            return 'You have entered wrong credentials.', 401
