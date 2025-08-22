


from functools import wraps
from flask import request, jsonify
from app.models.user import User
from extensions import db

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return jsonify({'message': 'API key is missing'}), 401
        
        current_user = db.session.query(User).filter_by(api_key=api_key).first()
        if not current_user:
            return jsonify({'message': 'Invalid API key'}), 401
        
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
