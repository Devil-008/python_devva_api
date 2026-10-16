from flask import Blueprint, request, jsonify
from app.models.user import db
from app.utils.auth import token_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

VALID_CURRENCIES = ['INR', 'USD', 'EUR', 'GBP', 'CAD', 'AUD', 'JPY']

@auth_bp.route('/profile', methods=['PUT'])
@token_required
def update_profile(current_user):
    data = request.get_json() or {}
    name = data.get('name')
    currency = data.get('currency')
    theme = data.get('theme')

    if name is not None and (not isinstance(name, str) or len(name.strip()) < 1 or len(name) > 100):
        return jsonify({'error': 'Name must be between 1 and 100 characters'}), 400
    
    if currency is not None and currency not in VALID_CURRENCIES:
        return jsonify({'error': 'Unsupported currency code'}), 400

    if theme is not None and theme not in ['light', 'dark']:
        return jsonify({'error': 'Theme must be light or dark'}), 400

    if name is not None:
        current_user.name = name.strip()
    if currency is not None:
        current_user.currency = currency
    if theme is not None:
        current_user.theme = theme

    db.session.commit()
    return jsonify({'message': 'Profile updated successfully.', 'user': current_user.to_dict()}), 200
