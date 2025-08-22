


from flask import jsonify, request
from app.models.shinobi import Shinobi
from app.schemas.shinobi_schema import ShinobiSchema
from extensions import db
from marshmallow import ValidationError
from util.reflection import populate_object

shinobi_schema = ShinobiSchema()
shinobis_schema = ShinobiSchema(many=True)

def get_all_shinobi():
    shinobis = Shinobi.query.all()
    return jsonify(shinobis_schema.dump(shinobis)), 200

def get_shinobi_by_id(shinobi_id):
    shinobi = Shinobi.query.get_or_404(shinobi_id)
    return jsonify(shinobi_schema.dump(shinobi)), 200

def create_shinobi():
    data = request.json
    try:
        new_shinobi = shinobi_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    db.session.add(new_shinobi)
    db.session.commit()
    return jsonify(shinobi_schema.dump(new_shinobi)), 201

def update_shinobi(shinobi_id):
    shinobi = Shinobi.query.get_or_404(shinobi_id)
    data = request.json
    try:
        updated_data = shinobi_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    resp = populate_object(shinobi, updated_data)
    if resp:
        return resp, 400
    db.session.commit()
    return jsonify(shinobi_schema.dump(shinobi)), 200

def delete_shinobi(shinobi_id):
    shinobi = Shinobi.query.get_or_404(shinobi_id)
    db.session.delete(shinobi)
    db.session.commit()
    return jsonify({'message': 'Shinobi deleted'}), 200
