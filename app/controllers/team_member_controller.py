

from app.models.team_member import TeamMember
from app.schemas.team_member_schema import TeamMemberSchema
from app.extensions import db
from marshmallow import ValidationError

team_member_schema = TeamMemberSchema()
team_members_schema = TeamMemberSchema(many=True)

def get_all_team_members():
    members = TeamMember.query.all()
    return team_members_schema.dump(members)

def get_team_member_by_id(member_id):
    member = TeamMember.query.get_or_404(member_id)
    return team_member_schema.dump(member)

def create_team_member(data):
    try:
        new_member = team_member_schema.load(data)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    db.session.add(new_member)
    db.session.commit()
    return team_member_schema.dump(new_member)

def update_team_member(member_id, data):
    member = TeamMember.query.get_or_404(member_id)
    try:
        updated_data = team_member_schema.load(data, partial=True)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    for key, value in updated_data.items():
        setattr(member, key, value)
    db.session.commit()
    return team_member_schema.dump(member)

def delete_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return {'message': 'Team member deleted'}


