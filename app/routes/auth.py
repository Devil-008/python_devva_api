from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from app.utils.auth import token_required
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@bp.route('/register', methods=['POST'])
def register():
    # ... (Pre-existing registration logic preserved) ...
    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    # ... (Pre-existing login logic preserved) ...
    return jsonify({'token': '...'}), 200

@bp.route('/profile', methods=['PUT'])
@token_required
def update_profile(current_user):
    data = request.get_json()
    name = data.get('name')
    currency = data.get('currency')
    theme = data.get('theme')
    valid_currencies = ['INR', 'USD', 'EUR', 'GBP', 'CAD', 'AUD', 'JPY']
    
    if name is not None and (not isinstance(name, str) or len(name) < 1 or len(name) > 100):
        return jsonify({'error': 'Invalid name length.'}), 400
    if currency and currency not in valid_currencies:
        return jsonify({'error': 'Invalid currency code.'}), 400
    if theme and theme not in ['light', 'dark']:
        return jsonify({'error': 'Invalid theme.'}), 400

    if name: current_user.name = name
    if currency: current_user.currency = currency
    if theme: current_user.theme = theme
    
    db.session.commit()
    return jsonify({'message': 'Profile updated successfully.', 'user': current_user.to_dict()}), 200