


from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.controllers.team_controller import (
    get_all_teams,
    get_team_by_id,
    create_team,
    update_team,
    delete_team
)

team_bp = Blueprint('team', __name__, url_prefix='/api/teams')

@team_bp.route('/', methods=['GET'])
def get_team_list():
    teams = get_all_teams()
    return jsonify(teams), 200

@team_bp.route('/<int:id>', methods=['GET'])
def get_team(id):
    team = get_team_by_id(id)
    return jsonify(team), 200

@team_bp.route('/', methods=['POST'])
def create_new_team():
    data = request.get_json()
    try:
        new_team = create_team(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(new_team), 201

@team_bp.route('/<int:id>', methods=['PUT'])
def update_existing_team(id):
    data = request.get_json()
    try:
        updated_team = update_team(id, data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    return jsonify(updated_team), 200

@team_bp.route('/<int:id>', methods=['DELETE'])
def delete_existing_team(id):
    result = delete_team(id)
    return jsonify(result), 200
