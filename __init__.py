

from flask import Flask
from config import Config
from .extensions import db, ma, bcrypt
from app.utils.error_handlers import register_error_handlers
import importlib
import pkgutil
from pathlib import Path

def register_blueprints(app):
    package_name = 'app.routes'
    package_path = Path(__file__).parent / 'routes'

    for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):
        module = importlib.import_module(f'{package_name}.{module_name}')
        # Try to get blueprint variable ending with '_bp'
        for attr in dir(module):
            if attr.endswith('_bp'):
                bp = getattr(module, attr)
                app.register_blueprint(bp)
                break

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    register_error_handlers(app)
    register_blueprints(app)

    return app


