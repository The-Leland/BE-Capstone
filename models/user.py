


from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    shinobi = db.relationship('Shinobi', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User id={self.id} username={self.username} email={self.email} role={self.role}>"
