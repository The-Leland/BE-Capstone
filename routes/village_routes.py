


from flask import Blueprint, request, jsonify
from app.models.village import Village
from app.schemas.village_schema import VillageSchema
from util.reflection import populate_object
from extensions import db

village_bp = Blueprint('village', __name__, url_prefix='/api/villages')
village_schema = VillageSchema()
villages_schema = VillageSchema(many=True)

@village_bp.route('/', methods=['GET'])
def get_villages():
    villages = Village.query.all()
    return villages_schema.jsonify(villages)

@village_bp.route('/<int:id>', methods=['GET'])
def get_village(id):
    village = Village.query.get_or_404(id)
    return village_schema.jsonify(village)

@village_bp.route('/', methods=['POST'])
def create_village():
    data = request.get_json()
    new_village = village_schema.load(data)
    db.session.add(new_village)
    db.session.commit()
    return village_schema.jsonify(new_village), 201

@village_bp.route('/<int:id>', methods=['PUT'])
def update_village(id):
    village = Village.query.get_or_404(id)
    data = request.get_json()
    error_response = populate_object(village, data)
    if error_response: 
        return error_response, 400
    db.session.commit()
    return village_schema.jsonify(village)

@village_bp.route('/<int:id>', methods=['DELETE'])
def delete_village(id):
    village = Village.query.get_or_404(id)
    db.session.delete(village)
    db.session.commit()
    return jsonify({'message': 'Village deleted'})
