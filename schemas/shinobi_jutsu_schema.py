

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.shinobi_jutsu import ShinobiJutsu
from app.schemas.shinobi_schema import ShinobiSchema
from app.schemas.jutsu_schema import JutsuSchema

class ShinobiJutsuSchema(SQLAlchemySchema):
    class Meta:
        model = ShinobiJutsu
        load_instance = True

    id = auto_field()
    shinobi_id = auto_field()
    jutsu_id = auto_field()
    mastery_level = auto_field()

    shinobi = fields.Nested(ShinobiSchema, dump_only=True)
    jutsu = fields.Nested(JutsuSchema, dump_only=True)
