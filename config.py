
# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY', 'your_super_secret_key_here')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///leaf_village.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
    



import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_super_secret_key_here')
    SQLALCHEMY_DATABASE_URI = (
        f"{os.environ.get('DATABASE_SCHEME')}"
        f"{os.environ.get('DATABASE_USER')}@"
        f"{os.environ.get('DATABASE_ADDRESS')}:"
        f"{os.environ.get('DATABASE_PORT')}/"
        f"{os.environ.get('DATABASE_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
    FLASK_PORT = int(os.environ.get('FLASK_PORT', 8086))
