


from flask import Blueprint, request, jsonify
from app.controllers.shinobi_controller import (
    get_all_shinobi,
    get_shinobi_by_id,
    create_shinobi,
    update_shinobi,
    delete_shinobi,
)
from app.schemas.shinobi_schema import ShinobiSchema
from app.utils.decorators import token_required, role_required

shinobi_bp = Blueprint('shinobi_bp', __name__)
shinobi_schema = ShinobiSchema()
shinobi_list_schema = ShinobiSchema(many=True)

@shinobi_bp.route('/', methods=['GET'])
@token_required
def get_shinobi(current_user):
    shinobi = get_all_shinobi()
    return shinobi_list_schema.jsonify(shinobi), 200

@shinobi_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_single_shinobi(current_user, id):
    shinobi = get_shinobi_by_id(id)
    return shinobi_schema.jsonify(shinobi), 200

@shinobi_bp.route('/', methods=['POST'])
@token_required
@role_required('admin')
def create_shinobi_route(current_user):
    data = request.get_json()
    try:
        new_shinobi = create_shinobi(data)
        return shinobi_schema.jsonify(new_shinobi), 201
    except Exception as e:
        return jsonify({'message': 'Error creating shinobi', 'error': str(e)}), 400

@shinobi_bp.route('/<int:id>', methods=['PUT'])
@token_required
@role_required('admin')
def update_shinobi_route(current_user, id):
    data = request.get_json()
    try:
        updated_shinobi = update_shinobi(id, data)
        return shinobi_schema.jsonify(updated_shinobi), 200
    except Exception as e:
        return jsonify({'message': 'Error updating shinobi', 'error': str(e)}), 400

@shinobi_bp.route('/<int:id>', methods=['DELETE'])
@token_required
@role_required('admin')
def delete_shinobi_route(current_user, id):
    try:
        message = delete_shinobi(id)
        return jsonify(message), 200
    except Exception as e:
        return jsonify({'message': 'Error deleting shinobi', 'error': str(e)}), 400
