from flask import Flask
from flask_migrate import Migrate

from . import database
from .web import models
from .web.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    database.db.init_app(app)
    db = database.db

    migrate = Migrate(app, db)

    @app.cli.command('db_create')
    def db_create():
        db.create_all()
        print("DB created")

    @app.cli.command('db_drop')
    def db_drop():
        db.drop_all()
        print('db dropped')

    @app.cli.command('insert_data')
    def insert_data():
        user1 = User(first_name='Ankan', last_name='Debnath', email='abcd@gmail.com',
                     password='1234')
        user2 = User(first_name='Diganta', last_name='Biswas', email='xyz@gmail.com',
                     password='1234')

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        print('data inserted')

    return app
