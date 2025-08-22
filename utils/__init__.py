

import importlib
import pkgutil
from pathlib import Path

def import_utils_modules():
    utils_path = Path(__file__).parent
    for _, module_name, _ in pkgutil.iter_modules([str(utils_path)]):
        if module_name == '__init__':
            continue
        importlib.import_module(f'app.utils.{module_name}')

import_utils_modules()
