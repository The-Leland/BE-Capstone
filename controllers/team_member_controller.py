

from flask import Blueprint, request, jsonify
from app.models.team_member import TeamMember
from app.schemas.team_member_schema import TeamMemberSchema
from extensions import db
from marshmallow import ValidationError
from util.reflection import populate_object

team_member_bp = Blueprint('team_member', __name__, url_prefix='/team-members')

team_member_schema = TeamMemberSchema()
team_members_schema = TeamMemberSchema(many=True)

@team_member_bp.route('/', methods=['GET'])
def get_team_members():
    members = TeamMember.query.all()
    return jsonify(team_members_schema.dump(members)), 200

@team_member_bp.route('/<int:member_id>', methods=['GET'])
def get_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    return jsonify(team_member_schema.dump(member)), 200

@team_member_bp.route('/', methods=['POST'])
def create_team_member():
    data = request.json
    try:
        new_member = team_member_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    db.session.add(new_member)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to create team member'}), 400
    return jsonify(team_member_schema.dump(new_member)), 201

@team_member_bp.route('/<int:member_id>', methods=['PUT'])
def update_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    data = request.json
    try:
        updated_data = team_member_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    resp = populate_object(member, updated_data)
    if resp:
        return resp, 400
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to update team member'}), 400
    return jsonify(team_member_schema.dump(member)), 200

@team_member_bp.route('/<int:member_id>', methods=['DELETE'])
def delete_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    db.session.delete(member)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to delete team member'}), 400
    return jsonify({'message': 'Team member deleted'}), 200

