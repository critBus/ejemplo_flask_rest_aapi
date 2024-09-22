from flask import Flask
from flask_migrate import Migrate
from .extencions import api ,db
from .resources import ns

def create_app():
    from .models import Course,Student
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    api.init_app(app)
    db.init_app(app)
    api.add_namespace(ns)
    migrate = Migrate(app, db)
    return app