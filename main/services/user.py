from main.repositories import UserRepository
from main.models import UserModel
from main.validators import email_validator

repository = UserRepository()


class User:
    """
        Acá va la lógica de negocio: llamar a un repo, hacer un cálculo, etc.
        Solamente ejecutan y devuelven algo.
    """

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
                plain_password=data["password"],
                username=data["username"]
            )
            repository.create_user(user_instance)
        except Exception as error:
            return error, 409


