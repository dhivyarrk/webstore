from flask import Flask
from flask_cors import CORS
from backend.config import DbConfig
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(DbConfig)
    CORS(app, origins=['http://localhost:3000'])
    return app