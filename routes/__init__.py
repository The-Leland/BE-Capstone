

import importlib
import pkgutil
from flask import Blueprint

def register_routes(app):
    package_name = __name__
    package_path = __path__

    for _, module_name, _ in pkgutil.iter_modules(package_path):
        if module_name == '__init__':
            continue
        module = importlib.import_module(f'{package_name}.{module_name}')
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, Blueprint):
                app.register_blueprint(attribute)
