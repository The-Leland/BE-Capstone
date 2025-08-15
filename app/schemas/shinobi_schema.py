

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.shinobi import Shinobi
from app.schemas.mission_schema import MissionSchema
from app.schemas.threat_profile_schema import ThreatProfileSchema
from app.schemas.shinobi_jutsu_schema import ShinobiJutsuSchema

class ShinobiSchema(SQLAlchemySchema):
    class Meta:
        model = Shinobi
        load_instance = True

    id = auto_field()
    name = auto_field()
    rank = auto_field()
    age = auto_field()
    village_id = auto_field()
    user_id = auto_field()
    threat_profile_id = auto_field()

    
    missions = fields.List(fields.Nested(MissionSchema, exclude=("assigned_shinobi",)))  
    threat_profile = fields.Nested(ThreatProfileSchema)
    shinobi_jutsu = fields.List(fields.Nested(ShinobiJutsuSchema))
