

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.nation import Nation

class NationSchema(SQLAlchemySchema):
    class Meta:
        model = Nation
        load_instance = True

    id = auto_field()
    name = auto_field()
    symbol = auto_field()
    
    villages = fields.List(fields.Nested('VillageSchema'), dump_only=True)
