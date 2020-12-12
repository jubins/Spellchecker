from flask import Flask
from flask_restful import Api, Resource, marshal_with
from flask_sqlalchemy import SQLAlchemy

from validators import GetTradeRequestArgs, PutTradeRequestArgs
from models import PricingModel, ResourceFields


app = Flask(__name__)
api = Api(app)

