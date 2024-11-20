from flask import Flask
from flask_cors import CORS
from backend.config import DbConfig
from flask_migrate import Migrate
from flask_cors import CORS
from backend.database import db
from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(DbConfig)
    CORS(app, origins=['http://localhost:3000'])

    db.init_app(app)
    migrate = Migrate(app, db)
    return app