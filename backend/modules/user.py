from flask import Blueprint, request, jsonify
from flask import g, current_app
from backend.database import db
from backend.models.webstoremodels import User
import flask_restful as restful
from werkzeug.security import generate_password_hash, check_password_hash
import json
from backend.modules.sesions import SessionCheckResource
import datetime
import random

class UserSignup(restful.Resource):
    def post(self):
        data = request.json

        try:
            hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
            new_user = User(
                #user_id=random.randint(0, 100),
                user_name=data['user_name'],
                password_hash=hashed_password,
                join_date=str(datetime.datetime.now()),
                membership=data.get('membership', 'regular'),
                contact_number=data.get('contact_number'),
                email_id=data['email_id'],
                user_type=data.get('user_type', 'customer')
            )
            print(new_user)
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email_id=data['email_id']).first()
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
        except Exception as e:
            return jsonify({"error": str(e)})