


from flask import Blueprint, request, jsonify
from app.models.nation import Nation
from app.schemas.nation_schema import NationSchema
from extensions import db
from marshmallow import ValidationError

nation_bp = Blueprint('nation', __name__, url_prefix='/nations')

nation_schema = NationSchema()
nations_schema = NationSchema(many=True)

@nation_bp.route('/', methods=['GET'])
def get_nations():
    nations = Nation.query.all()
    return jsonify(nations_schema.dump(nations))

@nation_bp.route('/<int:nation_id>', methods=['GET'])
def get_nation(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    return jsonify(nation_schema.dump(nation))

@nation_bp.route('/', methods=['POST'])
def create_nation():
    data = request.json
    try:
        new_nation = nation_schema.load(data)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    db.session.add(new_nation)
    db.session.commit()
    return jsonify(nation_schema.dump(new_nation)), 201

@nation_bp.route('/<int:nation_id>', methods=['PUT'])
def update_nation(nation_id):
    nation = Nation.query.get_or_404(nation_id)
    data = request.json
    try:
        updated_data = nation_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    for key, value in updated_data.items():
        setattr(nation, key, value)
    db.session.commit()
    return jsonify(nation_schema.dump(nation))

@nation_bp.route('/<int:nation_id>', methods=['DELETE'])
def delete_nation(nation_id):
    nation = N
