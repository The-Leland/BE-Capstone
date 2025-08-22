

from flask import Blueprint, request, jsonify
from app.models.jutsu import Jutsu
from app.schemas.jutsu_schema import JutsuSchema
from extensions import db

jutsu_bp = Blueprint('jutsu', __name__, url_prefix='/jutsu')

jutsu_schema = JutsuSchema()
jutsus_schema = JutsuSchema(many=True)

@jutsu_bp.route('/', methods=['GET'])
def get_jutsu():
    jutsus = Jutsu.query.all()
    return jsonify(jutsus_schema.dump(jutsus))

@jutsu_bp.route('/<int:jutsu_id>', methods=['GET'])
def get_jutsu_by_id(jutsu_id):
    jutsu = Jutsu.query.get_or_404(jutsu_id)
    return jsonify(jutsu_schema.dump(jutsu))

@jutsu_bp.route('/', methods=['POST'])
def create_jutsu():
    data = request.json
    new_jutsu = jutsu_schema.load(data)
    db.session.add(new_jutsu)
    db.session.commit()
    return jsonify(jutsu_schema.dump(new_jutsu)), 201

@jutsu_bp.route('/<int:jutsu_id>', methods=['PUT'])
def update_jutsu(jutsu_id):
    jutsu = Jutsu.query.get_or_404(jutsu_id)
    data = request.json
    for key, value in data.items():
        setattr(jutsu, key, value)
    db.session.commit()
    return jsonify(jutsu_schema.dump(jutsu))

@jutsu_bp.route('/<int:jutsu_id>', methods=['DELETE'])
def delete_jutsu(jutsu_id):
    jutsu = Jutsu.query.get_or_404(jutsu_id)
    db.session.delete(jutsu)
    db.session.commit()
    return jsonify({'message': 'Jutsu deleted'})
