# stdlib
import uuid

# database
from .. import db


class BaseModel(db.Model):
    """Base Model other models can extend """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime(), default=db.func.current_timestamp(), onupdate=db.func.now())

    def save(self):
        """Save a model to the database """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete a model from the database """
        db.session.delete(self)
        db.session.commit()
