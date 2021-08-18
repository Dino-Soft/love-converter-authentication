from sqlalchemy import sql
from werkzeug.security import check_password_hash, generate_password_hash

from main.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, index=True, nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    deleted = db.Column(db.Boolean, server_default=False)
    activated = db.Column(db.Boolean, server_default=False)
    last_updated = db.Column(db.DateTime, server_default=sql.func.now())
    last_access = db.Column(db.DateTime, server_default=sql.func.now())

    # Password security management
    @property
    def plain_password(self):
        raise AttributeError("The password can not be obtained. It is prohibited.")
        # We won't obtain the password accessing with a get method

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
        # We encrypt the plain text password from the JSON received in the user registration

    def validate_password(self, password):
        return check_password_hash(self.password, password)
        # Compares the received password with the database password

    # User object representation
    def __repr__(self):
        return f'<User: {self.id_num} {self.email} >'
