


from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.mission import Mission
from app.schemas.shinobi_schema import ShinobiSchema

class MissionSchema(SQLAlchemySchema):
    class Meta:
        model = Mission
        load_instance = True

    id = auto_field()
    title = auto_field()
    description = auto_field()
    rank = auto_field()
    assigned_shinobi_id = auto_field()
    status = auto_field()
    date_assigned = auto_field()

    assigned_shinobi = fields.Nested(ShinobiSchema, dump_only=True)

