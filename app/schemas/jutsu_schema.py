


from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.jutsu import Jutsu
from app.schemas.shinobi_jutsu_schema import ShinobiJutsuSchema

class JutsuSchema(SQLAlchemySchema):
    class Meta:
        model = Jutsu
        load_instance = True

    id = auto_field()
    name = auto_field()
    type = auto_field()
    description = auto_field()
    element = auto_field()
    difficulty_rank = auto_field()

    shinobi_jutsu = fields.List(fields.Nested(ShinobiJutsuSchema), dump_only=True)
