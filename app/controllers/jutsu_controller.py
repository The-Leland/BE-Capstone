

from app.models.jutsu import Jutsu
from app.schemas.jutsu_schema import JutsuSchema
from app.extensions import db

jutsu_schema = JutsuSchema()
jutsus_schema = JutsuSchema(many=True)

def get_all_jutsu():
    jutsus = Jutsu.query.all()
    return jutsus_schema.dump(jutsus)

def get_jutsu_by_id(jutsu_id):
    jutsu = Jutsu.query.get_or_404(jutsu_id)
    return jutsu_schema.dump(jutsu)

def create_jutsu(data):
    new_jutsu = jutsu_schema.load(data)
    db.session.add(new_jutsu)
    db.session.commit()
    return jutsu_schema.dump(new_jutsu)

def update_jutsu(jutsu_id, data):
    jutsu = Jutsu.query.get_or_404(jutsu_id)
    for key, value in data.items():
        setattr(jutsu, key, value)
    db.session.commit()
    return jutsu_schema.dump(jutsu)

def delete_jutsu(jutsu_id):
    jutsu = Jutsu.query.get_or_404(jutsu_id)
    db.session.delete(jutsu)
    db.session.commit()
    return {'message': 'Jutsu deleted'}


