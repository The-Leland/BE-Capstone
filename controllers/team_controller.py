


from flask import Blueprint, request, jsonify
from app.models.team import Team
from app.schemas.team_schema import TeamSchema
from extensions import db
from marshmallow import ValidationError

team_bp = Blueprint('team', __name__, url_prefix='/teams')

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)

@team_bp.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify(teams_schema.dump(teams))

@team_bp.route('/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = Team.query.get_or_404(team_id)
    return jsonify(team_schema.dump(team))

@team_bp.route('/', methods=['POST'])
def create_team():
    data = request.json
    try:
        new_team = team_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    db.session.add(new_team)
    db.session.commit()
    return jsonify(team_schema.dump(new_team)), 201

@team_bp.route('/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    team = Team.query.get_or_404(team_id)
    data = request.json
    try:
        updated_data = team_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    for key, value in updated_data.items():
        setattr(team, key, value)
    db.session.commit()
    return jsonify(team_schema.dump(team))

@team_bp.route('/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team deleted'})
