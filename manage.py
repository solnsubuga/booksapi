# standard lib
import os

# app
from api import create_app, db
from api.models import User, Book

default_config = os.getenv('DEFAULT_CONFIG', 'development')
app = create_app(default_config)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Book=Book)


if __name__ == '__main__':
    app.run()
