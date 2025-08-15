
from app.models.shinobi_jutsu import ShinobiJutsu
from app.schemas.shinobi_jutsu_schema import ShinobiJutsuSchema
from app.extensions import db
from marshmallow import ValidationError

shinobi_jutsu_schema = ShinobiJutsuSchema()
shinobi_jutsus_schema = ShinobiJutsuSchema(many=True)

def get_all_shinobi_jutsu():
    sj = ShinobiJutsu.query.all()
    return shinobi_jutsus_schema.dump(sj)

def get_shinobi_jutsu_by_id(sj_id):
    sj = ShinobiJutsu.query.get_or_404(sj_id)
    return shinobi_jutsu_schema.dump(sj)

def create_shinobi_jutsu(data):
    try:
        new_sj = shinobi_jutsu_schema.load(data)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    db.session.add(new_sj)
    db.session.commit()
    return shinobi_jutsu_schema.dump(new_sj)

def update_shinobi_jutsu(sj_id, data):
    sj = ShinobiJutsu.query.get_or_404(sj_id)
    try:
        updated_data = shinobi_jutsu_schema.load(data, partial=True)
    except ValidationError as err:
        return {'errors': err.messages}, 400
    for key, value in updated_data.items():
        setattr(sj, key, value)
    db.session.commit()
    return shinobi_jutsu_schema.dump(sj)

def delete_shinobi_jutsu(sj_id):
    sj = ShinobiJutsu.query.get_or_404(sj_id)
    db.session.delete(sj)
    db.session.commit()
    return {'message': 'ShinobiJutsu deleted'}

