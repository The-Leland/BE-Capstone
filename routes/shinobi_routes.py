


from flask import Blueprint, request, jsonify
from app.controllers.shinobi_controller import (
    get_all_shinobi,
    get_shinobi_by_id,
    create_shinobi,
    update_shinobi,
    delete_shinobi,
)
from app.schemas.shinobi_schema import ShinobiSchema

shinobi_bp = Blueprint('shinobi', __name__, url_prefix='/api/shinobi')
shinobi_schema = ShinobiSchema()
shinobi_list_schema = ShinobiSchema(many=True)

@shinobi_bp.route('/', methods=['GET'])
def get_shinobi():
    shinobi = get_all_shinobi()
    return shinobi_list_schema.jsonify(shinobi), 200

@shinobi_bp.route('/<int:id>', methods=['GET'])
def get_single_shinobi(id):
    shinobi = get_shinobi_by_id(id)
    return shinobi_schema.jsonify(shinobi), 200

@shinobi_bp.route('/', methods=['POST'])
def create_shinobi_route():
    data = request.get_json()
    try:
        new_shinobi = create_shinobi(data)
        return shinobi_schema.jsonify(new_shinobi), 201
    except Exception as e:
        return jsonify({'message': 'Error creating shinobi', 'error': str(e)}), 400

@shinobi_bp.route('/<int:id>', methods=['PUT'])
def update_shinobi_route(id):
    data = request.get_json()
    try:
        updated_shinobi = update_shinobi(id, data)
        return shinobi_schema.jsonify(updated_shinobi), 200
    except Exception as e:
        return jsonify({'message': 'Error updating shinobi', 'error': str(e)}), 400

@shinobi_bp.route('/<int:id>', methods=['DELETE'])
def delete_shinobi_route(id):
    try:
        message = delete_shinobi(id)
        return jsonify(message), 200
    except Exception as e:
        return jsonify({'message': 'Error deleting shinobi', 'error': str(e)}), 400
