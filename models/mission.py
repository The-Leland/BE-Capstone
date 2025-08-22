


from extensions import db

class Mission(db.Model):
    __tablename__ = 'missions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    rank = db.Column(db.String(2))
    assigned_shinobi_id = db.Column(db.Integer, db.ForeignKey('shinobi.id'))
    status = db.Column(db.String(20))
    date_assigned = db.Column(db.DateTime)

    assigned_shinobi = db.relationship('Shinobi', back_populates='missions')

    def __repr__(self):
        return f"<Mission id={self.id} title='{self.title}' rank='{self.rank}' status='{self.status}'>"
