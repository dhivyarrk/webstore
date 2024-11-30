import os

class DbConfig(object):
    #SQLALCHEMY_DATABASE_URI = "postgresql://webstore_user:12345@127.0.0.1:5432/webstore_database"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
