

from flask import Blueprint

from .user_routes import user_bp
from .nation_routes import nation_bp
from .village_routes import village_bp
from .shinobi_routes import shinobi_bp
from .threat_profile_routes import threat_profile_bp
from .jutsu_routes import jutsu_bp
from .shinobi_jutsu_routes import shinobi_jutsu_bp
from .mission_routes import mission_bp
from .team_routes import team_bp
from .team_member_routes import team_member_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(nation_bp, url_prefix='/api/nations')
    app.register_blueprint(village_bp, url_prefix='/api/villages')
    app.register_blueprint(shinobi_bp, url_prefix='/api/shinobi')
    app.register_blueprint(threat_profile_bp, url_prefix='/api/threat-profiles')
    app.register_blueprint(jutsu_bp, url_prefix='/api/jutsu')
    app.register_blueprint(shinobi_jutsu_bp, url_prefix='/api/shinobi-jutsu')
    app.register_blueprint(mission_bp, url_prefix='/api/missions')
    app.register_blueprint(team_bp, url_prefix='/api/teams')
    app.register_blueprint(team_member_bp, url_prefix='/api/team-members')


