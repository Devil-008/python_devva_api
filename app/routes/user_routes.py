from flask import Blueprint, request, jsonify
from app.services.user_service import update_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    data = request.get_json()
    user, error = update_user(user_id, data)
    if error:
        status = 404 if error == 'User not found' else 400
        return jsonify({'error': error}), status
    return jsonify(user.to_dict()), 200