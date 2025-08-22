


from app.models.shinobi import Shinobi
from app.schemas.shinobi_schema import ShinobiSchema
from app.extensions import db

shinobi_schema = ShinobiSchema()
shinobis_schema = ShinobiSchema(many=True)

def get_all_shinobi():
    shinobis = Shinobi.query.all()
    return shinobis_schema.dump(shinobis)

def get_shinobi_by_id(shinobi_id):
    shinobi = Shinobi.query.get_or_404(shinobi_id)
    return shinobi_schema.dump(shinobi)

def create_shinobi(data):
    new_shinobi = shinobi_schema.load(data)
    db.session.add(new_shinobi)
    db.session.commit()
    return shinobi_schema.dump(new_shinobi)

def update_shinobi(shinobi_id, data):
    shinobi = Shinobi.query.get_or_404(shinobi_id)
    for key, value in data.items():
        setattr(shinobi, key, value)
    db.session.commit()
    return shinobi_schema.dump(shinobi)

def delete_shinobi(shinobi_id):
    shinobi = Shinobi.query.get_or_404(shinobi_id)
    db.session.delete(shinobi)
    db.session.commit()
    return {'message': 'Shinobi deleted'}
