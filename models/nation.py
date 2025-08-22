

from extensions import db

class Nation(db.Model):
    __tablename__ = 'nations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    symbol = db.Column(db.String(120))
    villages = db.relationship('Village', back_populates='nation', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Nation id={self.id} name='{self.name}'>"
