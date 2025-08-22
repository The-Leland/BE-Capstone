


from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.models.user import User
from app.schemas.user_schema import UserSchema
from extensions import db

bp = Blueprint('auth', __name__, url_prefix='/auth')
user_schema = UserSchema()

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({'message': 'Username already exists'}), 400
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'message': 'Email already registered'}), 400
    
    password_hash = generate_password_hash(data.get('password'))
    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        password_hash=password_hash,
        role='user'
    )
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201
