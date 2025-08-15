


from app.models.team import Team
from app.schemas.team_schema import TeamSchema
from app.extensions import db
from marshmallow import ValidationError

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)

def get_all_teams():
    teams = Team.query.all()
    return teams_schema.dump(teams)

def get_team_by_id(team_id):
    team = Team.query.get_or_404(team_id)
    return team_schema.dump(team)

def create_team(data):
    try:
        new_team = team_schema.load(data)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    db.session.add(new_team)
    db.session.commit()
    return team_schema.dump(new_team)

def update_team(team_id, data):
    team = Team.query.get_or_404(team_id)
    try:
        updated_data = team_schema.load(data, partial=True)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    for key, value in updated_data.items():
        setattr(team, key, value)
    db.session.commit()
    return team_schema.dump(team)

def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return {'message': 'Team deleted'}

