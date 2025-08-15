


from flask import Blueprint, request, jsonify
from app.models.village import Village
from app.schemas.village_schema import VillageSchema
from app.extensions import db
from app.utils.decorators import token_required, role_required

village_bp = Blueprint('village_bp', __name__)
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
@token_required
@role_required('admin')
def create_village(current_user):
    data = request.get_json()
    new_village = village_schema.load(data)
    db.session.add(new_village)
    db.session.commit()
    return village_schema.jsonify(new_village), 201

@village_bp.route('/<int:id>', methods=['PUT'])
@token_required
@role_required('admin')
def update_village(current_user, id):
    village = Village.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(village, key, value)
    db.session.commit()
    return village_schema.jsonify(village)

@village_bp.route('/<int:id>', methods=['DELETE'])
@token_required
@role_required('admin')
def delete_village(current_user, id):
    village = Village.query.get_or_404(id)
    db.session.delete(village)
    db.session.commit()
    return jsonify({'message': 'Village deleted'})

