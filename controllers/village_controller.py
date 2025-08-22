

from flask import Blueprint, request, jsonify
from app.models.village import Village
from app.schemas.village_schema import VillageSchema
from extensions import db

village_bp = Blueprint('village', __name__, url_prefix='/villages')

village_schema = VillageSchema()
villages_schema = VillageSchema(many=True)

@village_bp.route('/', methods=['GET'])
def get_villages():
    villages = Village.query.all()
    return jsonify(villages_schema.dump(villages))

@village_bp.route('/<int:village_id>', methods=['GET'])
def get_village(village_id):
    village = Village.query.get_or_404(village_id)
    return jsonify(village_schema.dump(village))

@village_bp.route('/', methods=['POST'])
def create_village():
    data = request.json
    village = village_schema.load(data)
    db.session.add(village)
    db.session.commit()
    return jsonify(village_schema.dump(village)), 201

@village_bp.route('/<int:village_id>', methods=['PUT'])
def update_village(village_id):
    village = Village.query.get_or_404(village_id)
    data = request.json
    for key, value in data.items():
        setattr(village, key, value)
    db.session.commit()
    return jsonify(village_schema.dump(village))

@village_bp.route('/<int:village_id>', methods=['DELETE'])
def delete_village(village_id):
    village = Village.query.get_or_404(village_id)
    db.session.delete(village)
    db.session.commit()
    return jsonify({'message': 'Village deleted'})

