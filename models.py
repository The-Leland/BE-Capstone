


from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    shinobi = db.relationship('Shinobi', back_populates='user', cascade='all, delete-orphan')

class Nation(db.Model):
    __tablename__ = 'nations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    symbol = db.Column(db.String(120))
    villages = db.relationship('Village', back_populates='nation', cascade='all, delete-orphan')

class Village(db.Model):
    __tablename__ = 'villages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    symbol = db.Column(db.String(120))
    nation_id = db.Column(db.Integer, db.ForeignKey('nations.id'), nullable=False)
    kage_id = db.Column(db.Integer, db.ForeignKey('shinobi.id'), unique=True)
    nation = db.relationship('Nation', back_populates='villages')
    shinobi = db.relationship('Shinobi', back_populates='village', cascade='all, delete-orphan')
    kage = db.relationship('Shinobi', foreign_keys=[kage_id], uselist=False)

class ThreatProfile(db.Model):
    __tablename__ = 'threat_profiles'
    id = db.Column(db.Integer, primary_key=True)
    bounty = db.Column(db.Integer, default=0)
    threat_rank = db.Column(db.String(1))
    status = db.Column(db.String(50))
    shinobi = db.relationship('Shinobi', back_populates='threat_profile', uselist=False)

class Shinobi(db.Model):
    __tablename__ = 'shinobi'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(20))
    age = db.Column(db.Integer)
    village_id = db.Column(db.Integer, db.ForeignKey('villages.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    threat_profile_id = db.Column(db.Integer, db.ForeignKey('threat_profiles.id'), unique=True)
    village = db.relationship('Village', back_populates='shinobi')
    user = db.relationship('User', back_populates='shinobi')
    threat_profile = db.relationship('ThreatProfile', back_populates='shinobi')
    missions = db.relationship('Mission', back_populates='assigned_shinobi', cascade='all, delete-orphan')
    shinobi_jutsu = db.relationship('ShinobiJutsu', back_populates='shinobi', cascade='all, delete-orphan')
    team_members = db.relationship('TeamMember', back_populates='shinobi', cascade='all, delete-orphan')
    kage_village = db.relationship('Village', foreign_keys='Village.kage_id', uselist=False)

class Jutsu(db.Model):
    __tablename__ = 'jutsu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),
