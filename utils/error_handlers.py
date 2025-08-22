


import logging
from flask import Blueprint, jsonify, current_app
from marshmallow import ValidationError
import importlib
import pkgutil
from pathlib import Path

error_handlers_bp = Blueprint('error_handlers', __name__)

def handle_400(error):
    message = getattr(error, 'description', str(error))
    logging.warning(f"400 Bad Request: {message}")
    return jsonify({'error': 'Bad Request', 'message': message}), 400

def handle_401(error):
    message = getattr(error, 'description', str(error))
    logging.warning(f"401 Unauthorized: {message}")
    return jsonify({'error': 'Unauthorized', 'message': message}), 401

def handle_403(error):
    message = getattr(error, 'description', str(error))
    logging.warning(f"403 Forbidden: {message}")
    return jsonify({'error': 'Forbidden', 'message': message}), 403

def handle_404(error):
    logging.info("404 Not Found")
    return jsonify({'error': 'Resource not found'}), 404

def handle_500(error):
    logging.error("500 Internal Server Error", exc_info=True)
    if current_app.config.get('DEBUG'):
        return jsonify({'error': 'Server error', 'message': str(error)}), 500
    else:
        return jsonify({'error': 'Server error'}), 500

def handle_validation_error(error):
    logging.warning(f"Validation Error: {error.messages}")
    return jsonify({'error': 'Validation failed', 'messages': error.messages}), 400

def register_error_handlers(app):
    app.register_error_handler(400, handle_400)
    app.register_error_handler(401, handle_401)
    app.register_error_handler(403, handle_403)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(500, handle_500)
    app.register_error_handler(ValidationError, handle_validation_error)

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logging.error(f'Unhandled Exception: {error}', exc_info=True)
        if current_app.config.get('DEBUG'):
            return jsonify({'error': 'Unhandled Exception', 'message': str(error)}), 500
        else:
            return jsonify({'error': 'Server error'}), 500

def register_blueprint_and_errors(app):
    app.register_blueprint(error_handlers_bp)
    register_error_handlers(app)

def import_error_handlers():
    package_name = __name__
    package_path = Path(__file__).parent
    for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):
        if module_name == '__init__':
            continue
        importlib.import_module(f'{package_name}.{module_name}')

import_error_handlers()
