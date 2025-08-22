


from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.team_member import TeamMember
from app.schemas.team_schema import TeamSchema
from app.schemas.shinobi_schema import ShinobiSchema

class TeamMemberSchema(SQLAlchemySchema):
    class Meta:
        model = TeamMember
        load_instance = True

    id = auto_field()
    team_id = auto_field()
    shinobi_id = auto_field()
    role = auto_field()

    team = fields.Nested(TeamSchema, dump_only=True)
    shinobi = fields.Nested(ShinobiSchema, dump_only=True)
