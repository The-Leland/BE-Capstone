


from app.models.mission import Mission
from app.schemas.mission_schema import MissionSchema
from app.extensions import db

mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)

def get_all_missions():
    missions = Mission.query.all()
    return missions_schema.dump(missions)

def get_mission_by_id(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    return mission_schema.dump(mission)

def create_mission(data):
    new_mission = mission_schema.load(data)
    db.session.add(new_mission)
    db.session.commit()
    return mission_schema.dump(new_mission)

def update_mission(mission_id, data):
    mission = Mission.query.get_or_404(mission_id)
    for key, value in data.items():
        setattr(mission, key, value)
    db.session.commit()
    return mission_schema.dump(mission)

def delete_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    db.session.delete(mission)
    db.session.commit()
    return {'message': 'Mission deleted'}


