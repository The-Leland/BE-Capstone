



from flask import Blueprint, request, jsonify
from app.models.user import User
from app.schemas.user_schema import UserSchema
from extensions import db
from marshmallow import ValidationError
from util.reflection import populate_object

user_bp = Blueprint('user', __name__, url_prefix='/users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user_schema.dump(user)), 200

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = user_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    db.session.add(new_user)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to create user'}), 400
    return jsonify(user_schema.dump(new_user)), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    resp = populate_object(user, data)
    if resp:
        return resp, 400
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to update user'}), 400
    return jsonify(user_schema.dump(user)), 200

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to delete user'}), 400
    return jsonify({'message': 'User deleted'}), 200



