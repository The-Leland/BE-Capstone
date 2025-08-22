
from flask import Blueprint, request, jsonify
from app.models.shinobi_jutsu import ShinobiJutsu
from app.schemas.shinobi_jutsu_schema import ShinobiJutsuSchema
from extensions import db
from marshmallow import ValidationError
from util.reflection import populate_object

shinobi_jutsu_bp = Blueprint('shinobi_jutsu', __name__, url_prefix='/shinobi-jutsu')

shinobi_jutsu_schema = ShinobiJutsuSchema()
shinobi_jutsus_schema = ShinobiJutsuSchema(many=True)

@shinobi_jutsu_bp.route('/', methods=['GET'])
def get_shinobi_jutsu():
    sj = ShinobiJutsu.query.all()
    return jsonify(shinobi_jutsus_schema.dump(sj)), 200

@shinobi_jutsu_bp.route('/<int:sj_id>', methods=['GET'])
def get_shinobi_jutsu_by_id(sj_id):
    sj = ShinobiJutsu.query.get_or_404(sj_id)
    return jsonify(shinobi_jutsu_schema.dump(sj)), 200

@shinobi_jutsu_bp.route('/', methods=['POST'])
def create_shinobi_jutsu():
    data = request.json
    try:
        new_sj = shinobi_jutsu_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    db.session.add(new_sj)
    db.session.commit()
    return jsonify(shinobi_jutsu_schema.dump(new_sj)), 201

@shinobi_jutsu_bp.route('/<int:sj_id>', methods=['PUT'])
def update_shinobi_jutsu(sj_id):
    sj = ShinobiJutsu.query.get_or_404(sj_id)
    data = request.json
    try:
        updated_data = shinobi_jutsu_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    resp = populate_object(sj, updated_data)
    if resp:
        return resp, 400
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to update record'}), 400
    return jsonify(shinobi_jutsu_schema.dump(sj)), 200

@shinobi_jutsu_bp.route('/<int:sj_id>', methods=['DELETE'])
def delete_shinobi_jutsu(sj_id):
    sj = ShinobiJutsu.query.get_or_404(sj_id)
    db.session.delete(sj)
    db.session.commit()
    return jsonify({'message': 'ShinobiJutsu deleted'}), 200
