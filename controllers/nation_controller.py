


from flask import Blueprint, request, jsonify
from app.models.nation import Nation
from app.schemas.nation_schema import NationSchema
from extensions import db
from marshmallow import ValidationError
from util.reflection import populate_object

nation_bp = Blueprint('nation', __name__, url_prefix='/nations')

nation_schema = NationSchema()
nations_schema = NationSchema(many=True)

@nation_bp.route('/', methods=['GET'])
def get_nations():
    nations = Nation.query.all()
    return jsonify(nations_schema.dump(nations)), 200

@nation_bp.route('/<int:nation_id>', methods=['GET'])
def get_nation(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    return jsonify(nation_schema.dump(nation)), 200

@nation_bp.route('/', methods=['POST'])
def create_nation():
    data = request.json
    try:
        new_nation = nation_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    try:
        db.session.add(new_nation)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400
    return jsonify(nation_schema.dump(new_nation)), 201

@nation_bp.route('/<int:nation_id>', methods=['PUT'])
def update_nation(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    data = request.json
    try:
        updated_data = nation_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    resp = populate_object(nation, updated_data)
    if resp:
        return resp, 400
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to update record'}), 400
    return jsonify(nation_schema.dump(nation)), 200

@nation_bp.route('/<int:nation_id>', methods=['DELETE'])
def delete_nation(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    try:
        db.session.delete(nation)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'message': 'unable to delete record'}), 400
    return jsonify({'message': 'Nation deleted'}), 200
