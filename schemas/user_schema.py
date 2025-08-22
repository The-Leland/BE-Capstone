


from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields, validates, ValidationError
from app.models.user import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password_hash",)
    
    id = auto_field()
    username = auto_field(required=True)
    email = auto_field(required=True)
    role = auto_field()
    created_at = auto_field(dump_only=True)
    password = fields.String(load_only=True, required=True)

    @validates("email")
    def validate_email(self, value):
        if "@" not in value:
            raise ValidationError("Invalid email address.")




