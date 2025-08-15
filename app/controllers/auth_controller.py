


from flask import request, jsonify
from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.services.auth_services import verify_password, generate_auth_token

user_schema = UserSchema()

def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not verify_password(password, user.password_hash):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = generate_auth_token(user.id)

    return jsonify({
        'token': token,
        'user': user_schema.dump(user)
    }), 200


