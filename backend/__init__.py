from flask import Flask
from flask_cors import CORS
from backend.config import DbConfig
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

from backend.database import db
from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments
from backend.modules.sesions import SessionCheckResource
from backend.modules.user import UserSignup, UserList
from backend.modules.webstore import WomensclothesList, Womensclothes

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(DbConfig)
    CORS(app) #, origins=['http://localhost:3000'])

    init_api(app)
    return app

def init_api(app: Flask):
    db.init_app(app)

    migrate = Migrate(app, db)
    from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments
    api=Api(app)
    api.add_resource(UserList, '/users')
    api.add_resource(UserSignup, '/signup')
    api.add_resource(SessionCheckResource, '/session-check')
    #api.add_resource(UserSignin, '/signin')
    api.add_resource(WomensclothesList, '/womensclothes')
    api.add_resource(Womensclothes,  '/womensclothes/<string:product_id>', methods=['DELETE', 'PUT'])
