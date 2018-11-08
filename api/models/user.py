""" Module for the user model"""
# third party
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
# models
from .base_model import BaseModel
from .. import db


class User(BaseModel):
    __tablename__ = 'users'
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    books = db.relationship('Book', backref='owner', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        """Check if password is correct """
        return check_password_hash(self.password_hash, password)

    def generate_token(self):
        """ create a user token """
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=360000)
        return s.dumps({
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }).decode('ascii')

    def verify_token(self, token):
        """ verify a user token """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception:
            return None
        return User.query.get(data['id'])
