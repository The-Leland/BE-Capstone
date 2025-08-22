


from extensions import db

class ThreatProfile(db.Model):
    __tablename__ = 'threat_profiles'
    id = db.Column(db.Integer, primary_key=True)
    bounty = db.Column(db.Integer, default=0)
    threat_rank = db.Column(db.String(1))
    status = db.Column(db.String(50))
    
    shinobi = db.relationship('Shinobi', back_populates='threat_profile', uselist=False)

    def __repr__(self):
        return f"<ThreatProfile id={self.id} bounty={self.bounty} rank={self.threat_rank} status={self.status}>"
