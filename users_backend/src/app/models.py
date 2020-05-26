from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    token_count = db.Column(db.Integer, default=1, autoincrement=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    @classmethod
    def createUser(cls, email, password, first_name, last_name):
        user = cls(
            first_name=first_name,
            last_name=last_name,
            email=email, 
            password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def findUserByEmail(cls, email):
        return cls.query.filter_by(email=email).first()

    @property
    def token(self):
        self.token_count += 1
        db.session.commit()
        return create_access_token({'id': self.id, 'email': self.email, 'count': self.token_count})

    def isValidPassword(self, password):
        return check_password_hash(self.password, password)