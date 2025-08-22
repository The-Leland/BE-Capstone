


from flask import Blueprint, request, jsonify
from app.models.mission import Mission
from app.schemas.mission_schema import MissionSchema
from extensions import db

mission_bp = Blueprint('mission', __name__, url_prefix='/missions')

mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)

@mission_bp.route('/', methods=['GET'])
def get_missions():
    missions = Mission.query.all()
    return jsonify(missions_schema.dump(missions))

@mission_bp.route('/<int:mission_id>', methods=['GET'])
def get_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    return jsonify(mission_schema.dump(mission))

@mission_bp.route('/', methods=['POST'])
def create_mission():
    data = request.json
    new_mission = mission_schema.load(data)
    db.session.add(new_mission)
    db.session.commit()
    return jsonify(mission_schema.dump(new_mission)), 201

@mission_bp.route('/<int:mission_id>', methods=['PUT'])
def update_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    data = request.json
    for key, value in data.items():
        setattr(mission, key, value)
    db.session.commit()
    return jsonify(mission_schema.dump(mission))

@mission_bp.route('/<int:mission_id>', methods=['DELETE'])
def delete_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    db.session.delete(mission)
    db.session.commit()
    return jsonify({'message': 'Mission deleted'})
