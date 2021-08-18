
from main import db
from main.models import UserModel


class UserRepository:

    @staticmethod
    def get_user_by_id(id):
        try:
            user = db.session.query(UserModel).get_or_404(id)
        except Exception as e:
            print(f"Exception: \n{e}")
        return user

    @staticmethod
    def delete_user_by_id(id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        try:
            db.session.commit()
        except Exception as e:
            print(f"Exception: \n{e}")
            db.session.rollback()
            return False
        return True

    @staticmethod
    def edit_user_by_id(id, data):
        user = db.session.query(UserModel).get_or_404(id)
        for key, values in data:
            setattr(user, key, values)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

    @staticmethod
    def create_user(instance):
        db.session.add(instance)
        db.session.commit()
        return True
