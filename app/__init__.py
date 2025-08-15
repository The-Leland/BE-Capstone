

from flask import Flask
from config import Config
from .extensions import db, ma, jwt, bcrypt
from app.utils.error_handlers import register_error_handlers

from .routes.auth_routes import auth_bp
from .routes.user_routes import user_bp
from .routes.nation_routes import nation_bp
from .routes.village_routes import village_bp
from .routes.shinobi_routes import shinobi_bp
from .routes.jutsu_routes import jutsu_bp
from .routes.mission_routes import mission_bp
from .routes.team_routes import team_bp
from .routes.team_member_routes import team_member_bp
from .routes.threat_profile_routes import threat_profile_bp
from .routes.shinobi_jutsu_routes import shinobi_jutsu_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    register_error_handlers(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(nation_bp, url_prefix='/api/nations')
    app.register_blueprint(village_bp, url_prefix='/api/villages')
    app.register_blueprint(shinobi_bp, url_prefix='/api/shinobi')
    app.register_blueprint(jutsu_bp, url_prefix='/api/jutsu')
    app.register_blueprint(mission_bp, url_prefix='/api/missions')
    app.register_blueprint(team_bp, url_prefix='/api/teams')
    app.register_blueprint(team_member_bp, url_prefix='/api/team-members')
    app.register_blueprint(threat_profile_bp, url_prefix='/api/threat-profiles')
    app.register_blueprint(shinobi_jutsu_bp, url_prefix='/api/shinobi-jutsu')

    return app




