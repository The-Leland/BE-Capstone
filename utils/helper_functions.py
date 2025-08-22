

from datetime import datetime
import re
from flask import jsonify

def populate_object(obj, data_dictionary):
    for field in data_dictionary.keys():
        try:
            getattr(obj, field)
            setattr(obj, field, data_dictionary[field])
        except AttributeError:
            return jsonify({'message': f'attribute {field} not in object'})

def format_date(dt, fmt="%Y-%m-%d %H:%M:%S"):
    if not dt:
        return None
    return dt.strftime(fmt)

def parse_datetime(date_string, fmt="%Y-%m-%d %H:%M:%S"):
    try:
        return datetime.strptime(date_string, fmt)
    except (ValueError, TypeError):
        return None

def validate_email(email):
    if not email:
        return False
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

VALID_SHINOBI_RANKS = {'Genin', 'Chunin', 'Jonin', 'Kage', 'ANBU', 'Sannin'}

def validate_shinobi_rank(rank):
    return rank in VALID_SHINOBI_RANKS

def validate_jutsu_difficulty(difficulty):
    try:
        difficulty = int(difficulty)
        return 1 <= difficulty <= 10
    except (ValueError, TypeError):
        return False

ROLE_PERMISSIONS = {
    'admin': ['create', 'read', 'update', 'delete'],
    'shinobi': ['read', 'update'],
    'guest': ['read'],
}

def has_permission(role, action):
    permissions = ROLE_PERMISSIONS.get(role, [])
    return action in permissions

def validate_mastery_level(level):
    try:
        level = int(level)
        return 1 <= level <= 5
    except (ValueError, TypeError):
        return False

def get_dict_value_safe(data_dict, key, default=None):
    if not isinstance(data_dict, dict):
        return default
    return data_dict.get(key, default)
