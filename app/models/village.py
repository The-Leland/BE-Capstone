


from app.extensions import db

class Village(db.Model):
    __tablename__ = 'villages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    symbol = db.Column(db.String(120))
    nation_id = db.Column(db.Integer, db.ForeignKey('nations.id'), nullable=False)
    kage_id = db.Column(db.Integer, db.ForeignKey('shinobi.id'), unique=True)

    nation = db.relationship('Nation', back_populates='villages')
    shinobi = db.relationship('Shinobi', back_populates='village', cascade='all, delete-orphan', foreign_keys='Shinobi.village_id')
    kage = db.relationship('Shinobi', foreign_keys=[kage_id], uselist=False)

    def __repr__(self):
        return f"<Village id={self.id} name={self.name} nation_id={self.nation_id} kage_id={self.kage_id}>"


