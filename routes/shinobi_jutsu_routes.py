


from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.controllers.shinobi_jutsu_controller import (
    get_all_shinobi_jutsu,
    get_shinobi_jutsu_by_id,
    create_shinobi_jutsu,
    update_shinobi_jutsu,
    delete_shinobi_jutsu
)

shinobi_jutsu_bp = Blueprint('shinobi_jutsu', __name__, url_prefix='/api/shinobi-jutsu')

@shinobi_jutsu_bp.route('/', methods=['GET'])
def get_shinobi_jutsu_list():
    combos = get_all_shinobi_jutsu()
    return jsonify(combos), 200

@shinobi_jutsu_bp.route('/<int:id>', methods=['GET'])
def get_shinobi_jutsu(id):
    combo = get_shinobi_jutsu_by_id(id)
    if not combo:
        return jsonify({'message': 'Not found'}), 404
    return jsonify(combo), 200

@shinobi_jutsu_bp.route('/', methods=['POST'])
def create_new_shinobi_jutsu():
    data = request.get_json()
    try:
        new_combo = create_shinobi_jutsu(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(new_combo), 201

@shinobi_jutsu_bp.route('/<int:id>', methods=['PUT'])
def update_existing_shinobi_jutsu(id):
    data = request.get_json()
    try:
        updated_combo = update_shinobi_jutsu(id, data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(updated_combo), 200

@shinobi_jutsu_bp.route('/<int:id>', methods=['DELETE'])
def delete_existing_shinobi_jutsu(id):
    result = delete_shinobi_jutsu(id)
    return jsonify(result), 200
