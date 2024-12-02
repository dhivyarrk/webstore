from flask import Blueprint, request, jsonify
from flask import g, current_app
from backend.database import db
from backend.models.webstoremodels import KidsProducts
import flask_restful as restful
from werkzeug.security import generate_password_hash, check_password_hash
import json
import datetime
import random
from backend.modules.sesions import SessionCheckResource
from backend.models.webstoremodels import User


#import generate_token
#from flask_jwt_extended import jwt_required, get_jwt_identity



#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
blueprint = Blueprint('db1',__name__)

class KidsclothesList(restful.Resource):
    def get(self):
        token = request.headers.get('Authorization')  # Expecting token in headers
        if token and token.startswith('Bearer '):
            token = token.split(' ')[1]
            user_id = SessionCheckResource.verify_token(token)
            user = User.query.get(user_id)
            if user.user_type == 'admin' or user.user_type == 'customer' or user.user_type == 'employee':
                products = KidsProducts.query.filter_by(category_id=3).all()
                print(products)

                product_list = [product.to_dict() for product in products]  # Convert each object
                return jsonify(product_list)

            return jsonify("error: Unauthorized")

    def post(self):
        token = request.headers.get('Authorization')  # Expecting token in headers
        if token and token.startswith('Bearer '):
            token = token.split(' ')[1]
            user_id = SessionCheckResource.verify_token(token)
            user = User.query.get(user_id)
            if user.user_type == 'admin':
                data = request.json
                try:
                    new_product = KidsProducts(
                        product_name=data['productName'],
                        product_description=data['productDescription'],
                        product_price=data['productPrice'],
                        category_id=3,
                        availability=data.get('availability', 0)
                    )
                    db.session.add(new_product)
                    db.session.commit()
                    return jsonify({"message": "Product added successfully!"})
                except Exception as e:
                    return jsonify({"error": str(e)})
            return jsonify({"error": "Unauthorized"}), 401

class Kidsclothes(restful.Resource):
    def delete(self, product_id):
        token = request.headers.get('Authorization')  # Expecting token in headers
        if token and token.startswith('Bearer '):
            token = token.split(' ')[1]
            user_id = SessionCheckResource.verify_token(token)
            user = User.query.get(user_id)
            if user.user_type != 'admin':
                return jsonify({'message': 'Only admins can perform this action'}), 403

            # Find the product by ID
            product = KidsProducts.query.get(product_id)
            if not product:
                return jsonify({'message': 'Product not found'})

            # Delete the product
            db.session.delete(product)
            db.session.commit()
            return jsonify({'message': 'Product deleted successfully'})

    def put(self, product_id):
        token = request.headers.get('Authorization')  # Expecting token in headers
        if token and token.startswith('Bearer '):
            token = token.split(' ')[1]
            user_id = SessionCheckResource.verify_token(token)
            user = User.query.get(user_id)
            if user.user_type != 'admin':
                return jsonify({'message': 'Only admins can perform this action'})
            # Find the product by ID
            product = KidsProducts.query.get(product_id)
            if not product:
                return jsonify({'message': 'Product not found'})
            # Update product fields from request JSON
            data = request.json
            product.product_name = data.get('product_name', product.product_name)
            product.product_description = data.get('product_description', product.product_description)
            product.price = data.get('product_price', product.product_price)
            product.category_id = 3
            product.availability = data.get('availability', product.availability)
            db.session.commit()
            return jsonify({'message': 'Product updated successfully'})