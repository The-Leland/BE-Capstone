

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.team import Team
from app.schemas.shinobi_schema import ShinobiSchema
from app.schemas.village_schema import VillageSchema
from app.schemas.team_member_schema import TeamMemberSchema

class TeamSchema(SQLAlchemySchema):
    class Meta:
        model = Team
        load_instance = True

    id = auto_field()
    name = auto_field()
    leader_id = auto_field()
    village_id = auto_field()

    leader = fields.Nested(ShinobiSchema, dump_only=True)
    village = fields.Nested(VillageSchema, dump_only=True)
    members = fields.List(fields.Nested(TeamMemberSchema), dump_only=True)


