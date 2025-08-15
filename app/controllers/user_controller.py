



from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.extensions import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def get_all_users():
    users = User.query.all()
    return users_schema.dump(users)

def get_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    return user_schema.dump(user)

def create_user(data):
    new_user = user_schema.load(data)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user)

def update_user(user_id, data):
    user = User.query.get_or_404(user_id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user_schema.dump(user)

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted'}




