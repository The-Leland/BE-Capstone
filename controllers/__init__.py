

import os
import importlib
from flask import Blueprint

def register_controllers(app):
    controller_dir = os.path.dirname(__file__)
    for filename in os.listdir(controller_dir):
        if filename.endswith('_controller.py'):
            module_name = f"{__name__}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            for attr in dir(module):
                blueprint = getattr(module, attr)
                if isinstance(blueprint, Blueprint):
                    app.register_blueprint(blueprint)
