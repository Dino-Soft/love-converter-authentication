from re import I
from flask import request
from flask_restful import Resource
from main.extensions import db
from main.mappers import UserMapper
from main.models import UserModel
from main.validators import *
from werkzeug.security import generate_password_hash

user_mapper = UserMapper()


class Register(Resource):

    @staticmethod
    def post():
        json = request.get_json()
        
        # TODO Deshabilitado porque trae problemas -->> Corregir.
        
        if json != "":
            # TODO Deshabilitado porque trae problemas -->> Corregir.
            #if check_user(json["username"]) and check_password(json["password"]):
            
             # if check_email(json["email"]):
            email_validator(json["email"])
            
            # TODO aca se deberia encriptar la password...
            # user_repository.plain_password(json.get("password"))

            password_encrypted = generate_password_hash(json.get("password"))

            user_instance = UserModel(
                email=json.get("email"),
                password=password_encrypted,
                username=json.get("username"),
                deleted=False,
                activated=False,
                last_updated=json.get("last_updated"),
                last_access=json.get("last_access")
            )

            assert (user_instance.username is not None and user_instance.password is not None and
                    user_instance.email is not None, 'Username, password or email are required'
                    )

            db.session.add(user_instance)
            try:
                db.session.commit()
                return 'Done. Please activate your account in order to sign in', 201
            except Exception as error:
                db.session.rollback()
                print("\nUser operation error: ", error)
                return 'Error in operation', 409
