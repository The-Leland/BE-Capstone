


from app.extensions import db

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    leader_id = db.Column(db.Integer, db.ForeignKey('shinobi.id'), nullable=False)
    village_id = db.Column(db.Integer, db.ForeignKey('villages.id'))

    leader = db.relationship('Shinobi')
    village = db.relationship('Village')
    members = db.relationship('TeamMember', back_populates='team', cascade='all, delete-orphan')

def __repr__(self):
    return f"<Team {self.id} - {self.name}>"


