


from app.models.nation import Nation
from app.schemas.nation_schema import NationSchema
from app.extensions import db
from marshmallow import ValidationError

nation_schema = NationSchema()
nations_schema = NationSchema(many=True)

def get_all_nations():
    nations = Nation.query.all()
    return nations_schema.dump(nations)

def get_nation_by_id(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    return nation_schema.dump(nation)

def create_nation(data):
    try:
        new_nation = nation_schema.load(data)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    db.session.add(new_nation)
    db.session.commit()
    return nation_schema.dump(new_nation)

def update_nation(nation_id, data):
    nation = Nation.query.get_or_404(nation_id)
    try:
        updated_data = nation_schema.load(data, partial=True)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    for key, value in updated_data.items():
        setattr(nation, key, value)
    db.session.commit()
    return nation_schema.dump(nation)

def delete_nation(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    db.session.delete(nation)
    db.session.commit()
    return {'message': 'Nation deleted'}



