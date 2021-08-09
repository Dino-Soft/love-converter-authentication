from main.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, index=True, nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    deleted = db.Column(db.Boolean, nullable=False)
    activated = db.Column(db.Boolean, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    last_access = db.Column(db.DateTime, nullable=False)
    
    # User object representation
    def __repr__(self):
        return f'<User: {self.id_num} {self.email} >'
