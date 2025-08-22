

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.controllers.threat_profile_controller import (
    get_threat_profiles,
    get_threat_profile,
    create_threat_profile,
    update_threat_profile,
    delete_threat_profile
)

threat_profile_bp = Blueprint('threat_profile', __name__, url_prefix='/api/threat-profiles')

@threat_profile_bp.route('/', methods=['GET'])
def get_threat_profile_list():
    profiles = get_threat_profiles()
    return jsonify(profiles), 200

@threat_profile_bp.route('/<int:id>', methods=['GET'])
def get_threat_profile_by_id(id):
    profile = get_threat_profile(id)
    return jsonify(profile), 200

@threat_profile_bp.route('/', methods=['POST'])
def add_threat_profile():
    data = request.get_json()
    try:
        new_profile = create_threat_profile(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(new_profile), 201

@threat_profile_bp.route('/<int:id>', methods=['PUT'])
def modify_threat_profile(id):
    data = request.get_json()
    try:
        updated_profile = update_threat_profile(id, data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(updated_profile), 200

@threat_profile_bp.route('/<int:id>', methods=['DELETE'])
def remove_threat_profile(id):
    result = delete_threat_profile(id)
    return jsonify(result), 200
