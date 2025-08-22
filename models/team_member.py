
from extensions import db

class TeamMember(db.Model):
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    shinobi_id = db.Column(db.Integer, db.ForeignKey('shinobi.id'), nullable=False)
    role = db.Column(db.String(20))

    team = db.relationship('Team', back_populates='members')
    shinobi = db.relationship('Shinobi', back_populates='team_members')

    def __repr__(self):
        return f"TeamMember {self.id} - Role: {self.role}>"
