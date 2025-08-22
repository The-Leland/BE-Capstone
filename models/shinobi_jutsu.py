

from extensions import db

class ShinobiJutsu(db.Model):
    """Association table linking Shinobi and Jutsu with mastery level info."""
    
    __tablename__ = 'shinobi_jutsu'

    id = db.Column(db.Integer, primary_key=True)
    shinobi_id = db.Column(db.Integer, db.ForeignKey('shinobi.id'), nullable=False)
    jutsu_id = db.Column(db.Integer, db.ForeignKey('jutsu.id'), nullable=False)
    mastery_level = db.Column(db.String(20))

    shinobi = db.relationship('Shinobi', back_populates='shinobi_jutsu')
    jutsu = db.relationship('Jutsu', back_populates='shinobi_jutsu')

    def __repr__(self):
        return (
            f"<ShinobiJutsu id={self.id} shinobi_id={self.shinobi_id} "
            f"jutsu_id={self.jutsu_id} mastery_level={self.mastery_level}>"
        )

