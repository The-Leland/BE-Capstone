


from functools import wraps
from flask import request, jsonify
import jwt
from app.models.user import User
from app.extensions import db
from flask import current_app as app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = db.session.get(User, data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, *args, **kwargs):
            if current_user.role != required_role:
                return jsonify({'message': 'Access forbidden: insufficient permissions'}), 403
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator


