


from app.extensions import db

class Shinobi(db.Model):
    __tablename__ = 'shinobi'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(20))
    age = db.Column(db.Integer)
    village_id = db.Column(db.Integer, db.ForeignKey('villages.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    threat_profile_id = db.Column(db.Integer, db.ForeignKey('threat_profiles.id'), unique=True)

    village = db.relationship('Village', back_populates='shinobi', foreign_keys=[village_id])
    user = db.relationship('User', back_populates='shinobi')
    threat_profile = db.relationship('ThreatProfile', back_populates='shinobi')
    missions = db.relationship('Mission', back_populates='assigned_shinobi', cascade='all, delete-orphan')
    shinobi_jutsu = db.relationship('ShinobiJutsu', back_populates='shinobi', cascade='all, delete-orphan')
    team_members = db.relationship('TeamMember', back_populates='shinobi', cascade='all, delete-orphan')
    kage_village = db.relationship('Village', foreign_keys='Village.kage_id', uselist=False)

    def __repr__(self):
        return f"<Shinobi {self.name} (Rank: {self.rank})>"


