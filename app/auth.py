from flask import request, jsonify
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
import jwt
import datetime
from app import db

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, 'SECRET_KEY', algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def create_user(data):
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(email=data['email'], name=data['name'], mobile=data['mobile'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

def login(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed!'}), 401
    token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'SECRET_KEY')
    return jsonify({'token': token})
