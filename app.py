

from flask import Flask
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv

from db import init_db, db
from util.blueprints import register_blueprints

load_dotenv()

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_PORT")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")  # Only this is needed
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

register_blueprints(app)

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(host=flask_host, port=int(flask_port), debug=True)
