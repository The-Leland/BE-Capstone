


from flask import Blueprint, request, jsonify
from app.controllers.user_controller import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user
)

user_bp = Blueprint('user', __name__, url_prefix='/api/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = get_user_by_id(id)
    return jsonify(user)

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.json
    user = create_user(data)
    return jsonify(user), 201

@user_bp.route('/<int:id>', methods=['PUT'])
def modify_user(id):
    data = request.json
    user = update_user(id, data)
    return jsonify(user)

@user_bp.route('/<int:id>', methods=['DELETE'])
def remove_user(id):
    result = delete_user(id)
    return jsonify(result)
