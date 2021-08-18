from main.repositories import UserRepository
from main.models import UserModel
from main.validators import email_validator


repository = UserRepository()


class User:

    @staticmethod
    def get_user_by_id(id):
        repository.get_user_by_id(id)

    @staticmethod
    def delete_user_by_id(id):
        repository.delete_user_by_id(id)

    @staticmethod
    def edit_user_by_id(id, data):
        repository.edit_user_by_id(id, data)

    @staticmethod
    def add_user(data):
        # Verify if the email exists
        email_validator(data["email"])

        try:
            # Generate user instance
            user_instance = UserModel(
                email=data["email"],
                username=data["username"]
            )

            user_instance.plain_password(data["password"])

            repository.create_user(user_instance)
        except Exception as error:
            return error, 409
