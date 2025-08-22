


from extensions import db, ma

class Jutsu(db.Model):
    __tablename__ = 'jutsu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    description = db.Column(db.Text)
    element = db.Column(db.String(20))
    difficulty_rank = db.Column(db.String(1))
    shinobi_jutsu = db.relationship('ShinobiJutsu', back_populates='jutsu', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Jutsu id={self.id} name='{self.name}' type='{self.type}' element='{self.element}' difficulty='{self.difficulty_rank}'>"

class JutsuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jutsu
        load_instance = True
        include_fk = True

jutsu_schema = JutsuSchema()
jutsus_schema = JutsuSchema(many=True)

