from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
api = Api(version='1.0', title='Mi App')
db = SQLAlchemy()