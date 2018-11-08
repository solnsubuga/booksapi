""" Module for the book model"""
# models
from .base_model import BaseModel
from .. import db


class Book(BaseModel):
    """ Book model """
    __tablename__ = 'books'
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
