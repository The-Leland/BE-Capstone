


from flask import Blueprint, request, jsonify
from app.models.user import User
from app.schemas.user_schema import UserSchema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
user_schema = UserSchema()

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or user.password_hash != password:
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({
        'user': user_schema.dump(user)
    }), 200
