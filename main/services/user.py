from werkzeug.security import check_password_hash, generate_password_hash

from main.extensions import db
from main.repositories import UserRepository

repository = UserRepository()


class User:
    """
        Acá va la lógica de negocio: llamar a un repo, hacer un cálculo, etc.
        Solamente ejecutan y devuelven algo.
    """

    # Password security management
    @staticmethod
    def plain_password():
        repository.plain_password()

    @staticmethod
    def plain_password(password):
        repository.plain_password(password)

    @staticmethod
    def validate_password(password):
        repository.validate_password(password)

    @staticmethod
    def get_user_by_id(id):
        repository.get_register_by_id(id)

    @staticmethod
    def delete_user_by_id(id):
        repository.delete_register_by_id(id)

    @staticmethod
    def edit_user_by_id(id, data):
        repository.edit_register_by_id(id, data)

    @staticmethod
    def add_user(email, data):
        repository.create_register(email, data)
