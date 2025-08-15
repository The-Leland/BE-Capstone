
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_super_secret_key_here')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///leaf_village.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-string')

