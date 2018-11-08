"""module for setting up fixtures"""

import pytest

from api import create_app, db
from api.models import User, Book


@pytest.yield_fixture(scope='session')
def app():
    _app = create_app('testing')
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    yield app.test_client()


@pytest.fixture(scope='function')
def set_db(app):
    db.create_all()
    yield db
    db.session.close()
    db.drop_all()


@pytest.fixture(scope='function')
def new_user():
    return User(
        name='test',
        email='test@test.com',
        password='test'
    )


@pytest.fixture(scope='function')
def new_book(new_user):
    new_user.save()
    return Book(
        name='Advanced Cloud Native Go',
        description='Lorem ipsum is the best placeholder text',
        owner=new_user
    )
