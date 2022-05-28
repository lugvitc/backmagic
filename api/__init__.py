from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

api = Flask(__name__)
cors ==CORS(api)

api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api)

from api.models import *
db.create_all()

from api.endpoints import *