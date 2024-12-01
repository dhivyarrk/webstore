from flask import Flask
from flask_cors import CORS
from backend.config import DbConfig
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

from backend.database import db
from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments
from backend.modules.sesions import SessionCheckResource
from backend.modules.user import UserSignup, UserList, UserSignin
from backend.modules.womensclothes import WomensclothesList, Womensclothes
from backend.modules.womensaccessories import WomensaccessoriesList, Womensaccessories
from backend.modules.kidsclothes import KidsclothesList, Kidsclothes
from backend.modules.kidsshoes import KidsshoesList, Kidsshoes

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(DbConfig)
    CORS(app)
    #CORS(app, supports_credentials=True, origins=["http://127.0.0.1:4200", "http://localhost:4200/"])
    #CORS(app, supports_credentials=True, origins="https://booboofashions.netlify.app/")
   
     #, origins=['http://localhost:3000'])

    #init_api(app)
    db.init_app(app)

    migrate = Migrate(app, db)
    from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments
    api=Api(app)
    api.add_resource(UserList, '/users')
    api.add_resource(UserSignup, '/signup')
    api.add_resource(SessionCheckResource, '/session-check')
    api.add_resource(UserSignin, '/signin')
    api.add_resource(WomensclothesList, '/womensclothes')
    api.add_resource(Womensclothes,  '/womensclothes/<string:product_id>', methods=['DELETE', 'PUT'])
    api.add_resource(WomensaccessoriesList, '/womensaccessories')
    api.add_resource(Womensaccessories,  '/womensaccessories/<string:product_id>', methods=['DELETE', 'PUT'])
    api.add_resource(KidsclothesList, '/kidsclothes')
    api.add_resource(Kidsclothes,  '/kidsclothes/<string:product_id>', methods=['DELETE', 'PUT'])
    api.add_resource(KidsshoesList, '/kidsshoes')
    api.add_resource(Kidsshoes,  '/kidsshoes/<string:product_id>', methods=['DELETE', 'PUT'])

    return app
"""
def init_api(app: Flask):
    db.init_app(app)

    migrate = Migrate(app, db)
    from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments
    api=Api(app)
    api.add_resource(UserList, '/users')
    api.add_resource(UserSignup, '/signup')
    api.add_resource(SessionCheckResource, '/session-check')
    api.add_resource(UserSignin, '/signin')
    api.add_resource(WomensclothesList, '/womensclothes')
    api.add_resource(Womensclothes,  '/womensclothes/<string:product_id>', methods=['DELETE', 'PUT'])
"""