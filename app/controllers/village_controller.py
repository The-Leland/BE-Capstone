

from app.models.village import Village
from app.schemas.village_schema import VillageSchema
from app.extensions import db

village_schema = VillageSchema()
villages_schema = VillageSchema(many=True)

def get_all_villages():
    villages = Village.query.all()
    return villages_schema.dump(villages)

def get_village_by_id(village_id):
    village = Village.query.get_or_404(village_id)
    return village_schema.dump(village)

def create_village(data):
    village = village_schema.load(data)
    db.session.add(village)
    db.session.commit()
    return village_schema.dump(village), 201

def update_village(village_id, data):
    village = Village.query.get_or_404(village_id)
    for key, value in data.items():
        setattr(village, key, value)
    db.session.commit()
    return village_schema.dump(village)

def delete_village(village_id):
    village = Village.query.get_or_404(village_id)
    db.session.delete(village)
    db.session.commit()
    return {'message': 'Village deleted'}, 200
