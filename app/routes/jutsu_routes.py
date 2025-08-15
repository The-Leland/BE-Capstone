


from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.controllers.jutsu_controller import (
    get_all_jutsu,
    get_jutsu_by_id,
    create_jutsu,
    update_jutsu,
    delete_jutsu
)

jutsu_bp = Blueprint('jutsu_bp', __name__)

@jutsu_bp.route('/', methods=['GET'])
def get_jutsu_list():
    jutsus = get_all_jutsu()
    return jsonify(jutsus), 200

@jutsu_bp.route('/<int:id>', methods=['GET'])
def get_jutsu(id):
    jutsu = get_jutsu_by_id(id)
    return jsonify(jutsu), 200

@jutsu_bp.route('/', methods=['POST'])
def create_new_jutsu():
    data = request.get_json()
    try:
        new_jutsu = create_jutsu(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(new_jutsu), 201

@jutsu_bp.route('/<int:id>', methods=['PUT'])
def update_existing_jutsu(id):
    data = request.get_json()
    try:
        updated_jutsu = update_jutsu(id, data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(updated_jutsu), 200

@jutsu_bp.route('/<int:id>', methods=['DELETE'])
def delete_existing_jutsu(id):
    result = delete_jutsu(id)
    return jsonify(result), 200


