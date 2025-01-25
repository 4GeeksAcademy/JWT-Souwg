
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, BlockedTokenList
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt


app = Flask(__name__)
bcrypt = Bcrypt(app)

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

{
    "email": "pingu@pingu.com",
    "password": "123456"
}

@api.route('/signup', methods=['POST'])
def register_user():
    body=request.get_json()
    # Make routine verifications
    email = body.get('email')
    password = body.get('password')
    user_exists = User.query.filter_by(email=email).first()
    if user_exists:
        return jsonify({"msg": "Email already registered"})
    if not email:
        return jsonify({'msg': "Need Email"}),400
    if not password:
        return jsonify({'msg': "Need Password"}),400
    # Encrypt password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(email=email, password=hashed_password, is_active=True)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg":"Usuario registrado Exitosamente"})

@api.route('/login', methods=['POST'])
def login_user():
    body=request.get_json()
    email = body.get('email')
    password = body.get('password')
    if not email:
        return jsonify({'msg': "Need Email"}),400
    if not password:
        return jsonify({'msg': "Need Password"}),400
    
    user= User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"msg": "User not Found"}),404
    
    valid_password = bcrypt.check_password_hash(user.password, password)
    if not valid_password:
        return jsonify({"msg": "Invalid Credentials"})
    
    acces_token = create_access_token(identity=user.id)
    return jsonify({"token": acces_token})

@api.route('/userinfo', methods=['GET'])
@jwt_required()
def private_info():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({"userInfo":user.serialize()}),200

@api.route('/logout', methods=['POST'])
@jwt_required()
def user_logout():
    token = get_jwt()
    blocked_token = BlockedTokenList(jti=token["jti"])
    db.session.add(blocked_token)
    db.session.commit()
    return jsonify({"msg":"Session cerrada"})
