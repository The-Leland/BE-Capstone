

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.village import Village

class VillageSchema(SQLAlchemySchema):
    class Meta:
        model = Village
        load_instance = True

    id = auto_field()
    name = auto_field()
    symbol = auto_field()
    nation_id = auto_field()
    kage_id = auto_field()

    nation = fields.Nested('NationSchema', dump_only=True)
    kage = fields.Nested('ShinobiSchema', dump_only=True)

