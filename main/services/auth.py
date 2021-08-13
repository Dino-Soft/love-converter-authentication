from main.repositories import UserRepository
from main.models import UserModel
from main.validators import email_validator

repository = UserRepository()


class Auth:
    """
        Acá va la lógica de negocio: llamar a un repo, hacer un cálculo, etc.
        Solamente ejecutan y devuelven algo.
    """

    @staticmethod
    def login(id):
        pass

    @staticmethod
    def logout(id):
        pass



