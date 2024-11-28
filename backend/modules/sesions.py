import flask_restful as restful
import jwt
import datetime

SECRET_KEY = 'your_secret_key'  # Replace with a strong secret key

# Check session resource
class SessionCheckResource(restful.Resource):
    # Generate JWT token
    def generate_token(user_id):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
        payload = {
            'user_id': user_id,
            'exp': expiration
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    # Verify JWT token
    def verify_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
            #return payload
        except jwt.ExpiredSignatureError:
            return None  # Token expired
        except jwt.InvalidTokenError:
            return None  # Invalid token
