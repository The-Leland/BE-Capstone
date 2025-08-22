

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.threat_profile import ThreatProfile
from app.schemas.shinobi_schema import ShinobiSchema

class ThreatProfileSchema(SQLAlchemySchema):
    class Meta:
        model = ThreatProfile
        load_instance = True

    id = auto_field()
    bounty = auto_field()
    threat_rank = auto_field()
    status = auto_field()

    shinobi = fields.Nested(ShinobiSchema, dump_only=True)
