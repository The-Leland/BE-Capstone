



from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.controllers.mission_controller import (
    get_all_missions,
    get_mission_by_id,
    create_mission,
    update_mission,
    delete_mission
)

mission_bp = Blueprint('mission_bp', __name__)

@mission_bp.route('/', methods=['GET'])
def get_mission_list():
    missions = get_all_missions()
    return jsonify(missions), 200

@mission_bp.route('/<int:id>', methods=['GET'])
def get_mission(id):
    mission = get_mission_by_id(id)
    return jsonify(mission), 200

@mission_bp.route('/', methods=['POST'])
def create_new_mission():
    data = request.get_json()
    try:
        new_mission = create_mission(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(new_mission), 201

@mission_bp.route('/<int:id>', methods=['PUT'])
def update_existing_mission(id):
    data = request.get_json()
    try:
        updated_mission = update_mission(id, data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(updated_mission), 200

@mission_bp.route('/<int:id>', methods=['DELETE'])
def delete_existing_mission(id):
    result = delete_mission(id)
    return jsonify(result), 200
