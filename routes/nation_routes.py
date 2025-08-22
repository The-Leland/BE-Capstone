


from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.controllers.nation_controller import (
    get_all_nations,
    get_nation_by_id,
    create_nation,
    update_nation,
    delete_nation
)

nation_bp = Blueprint('nation', __name__, url_prefix='/api/nations')

@nation_bp.route('/', methods=['GET'])
def get_nation_list():
    nations = get_all_nations()
    return jsonify(nations), 200

@nation_bp.route('/<int:id>', methods=['GET'])
def get_nation(id):
    nation = get_nation_by_id(id)
    return jsonify(nation), 200

@nation_bp.route('/', methods=['POST'])
def create_new_nation():
    data = request.get_json()
    try:
        new_nation = create_nation(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(new_nation), 201

@nation_bp.route('/<int:id>', methods=['PUT'])
def update_existing_nation(id):
    data = request.get_json()
    try:
        updated_nation = update_nation(id, data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(updated_nation), 200

@nation_bp.route('/<int:id>', methods=['DELETE'])
def delete_existing_nation(id):
    result = delete_nation(id)
    return jsonify(result), 200
