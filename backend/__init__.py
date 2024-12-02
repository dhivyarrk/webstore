from flask import Flask, jsonify
from flask_cors import CORS
from backend.config import DbConfig
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask import Flask, session, redirect, url_for, request
from werkzeug.security import generate_password_hash

from backend.database import db
from backend.models.webstoremodels import User, WomensProducts, KidsProducts, Categories, Orders, Shipments
from backend.modules.sesions import SessionCheckResource
from backend.modules.user import UserSignup, UserList, UserSignin
from backend.modules.womensclothes import WomensclothesList, Womensclothes
from backend.modules.womensaccessories import WomensaccessoriesList, Womensaccessories
from backend.modules.kidsclothes import KidsclothesList, Kidsclothes
from backend.modules.kidsshoes import KidsshoesList, Kidsshoes
from authlib.integrations.flask_client import OAuth
from flask_session import Session

import os
import datetime
#import random

s_value = "something"
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )

    app.secret_key = 'your_secret_key_here'

# Configure server-side session
    app.config['SESSION_TYPE'] = 'filesystem'  # Options: 'redis', 'memcached', etc.
    app.config['SESSION_PERMANENT'] = True    # Optional: set to True if sessions should persist across browser restarts
    Session(app)
    app.config.from_object(DbConfig)
    CORS(app, supports_credentials=True)
    #CORS(app, supports_credentials=True, origins=["http://127.0.0.1:4200", "http://localhost:4200/"])
    #CORS(app, supports_credentials=True, origins="https://booboofashions.netlify.app/")
   
     #, origins=['http://localhost:3000'])

    #init_api(app)
    oauth = OAuth(app)

    
    oauth.register(
    name= 'idp',
    
    #name='flask-app-project-442612',  # Name of your IdP
    client_id=os.getenv('client_id'),
    client_secret=os.getenv('client_secret'),
    access_token_url=os.getenv('access_token_url'),
    authorize_url=os.getenv('authorize_url'),
    #api_base_url='https://idp.com/api',
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url= os.getenv('server_metadata_url')
    )
    

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

    @app.route('/login')
    def login():
        print("i am in login")
        #return 'this is login'
        #return oauth.idp.authorize_redirect(redirect_uri='https://booboofashionsgunic.onrender.com/callback')
        #return oauth.idp.authorize_redirect(redirect_uri='http://localhost:5000/callback')
        redirect_uri = url_for('callback', _external=True)
        return oauth.idp.authorize_redirect(redirect_uri=redirect_uri)


    @app.route('/callback')
    def callback():
        if session.get('state') != request.args.get('state'):
            print("State mismatch! CSRF detected. 400")
        token = oauth.idp.authorize_access_token()
        user_info = token['userinfo']
        #user_info = oauth.idp.parse_id_token(token)
        session['user'] = user_info
        #print(session)
        global userinfo
        userinfo = session['user']
        #print("incallabacl")
        #print(userinfo)
        #dummy contact_number to avoid gathering personal info for now
        #contact_number = random.randint(10**((random.randint(1, 15)) - 1), 10**(random.randint(1, 15)) - 1)
        try:
            user = User.query.filter_by(email_id=token['userinfo']["email"]).first()
            if user:
                #return redirect('http://localhost:4200/callback')
                return redirect('https://booboofashions.netlify.app/callback')
            else:
                hashed_password = generate_password_hash("12345", method='pbkdf2:sha256') # Todo: dummy password
                new_user = User(
                    #user_id=random.randint(0, 100),
                    user_name=token["userinfo"]["name"],
                    password_hash=hashed_password,
                    join_date=str(datetime.datetime.now()),
                    membership='regular',
                    contact_number=123, #Todo: dummy info to avoid storing personal info
                    email_id=token["userinfo"]["email"],
                    user_type='customer'
                )
                #print(new_user)
                db.session.add(new_user)
                db.session.commit()
                #return redirect('http://localhost:4200/callback')
                return redirect('https://booboofashions.netlify.app/callback')

        except Exception as e:
            return jsonify({"error": str(e)})


    @app.route('/user_info')
    def user_info():
        try:
            print("in user_info")
            print(userinfo)
            user = User.query.filter_by(email_id=userinfo["email"]).first()
            if user:
                token = SessionCheckResource.generate_token(user.user_id)
                return jsonify({
                    "message": "User created successfully!",
                    "user": {
                        "user_name": user.user_name,
                        "membership": user.membership,
                        "user_type": user.user_type,
                        "email_id": user.email_id,
                        "token": token
                    }
                })

                #return redirect('http://localhost:4200/callback')
                #return redirect(f'http://localhost:4200/callback?user_info={userinfo}')

        except Exception as e:
            return jsonify({"error": str(e)})
        #return redirect('https://booboofashions.netlify.app/dashboard')
        #return redirect('http://localhost:4200/dashboard')


    @app.route('/logout')
    def logout():
        session.pop('user', None)
        #return redirect('https://booboofashions.netlify.app/dashboard/')
        #return redirect('http://localhost:4200/dashboard')
        return redirect('https://booboofashions.netlify.app/dashboard')

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