from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, update_user
from app.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user, error = create_user(data.get('name'), data.get('email'), data.get('password'))
    if error:
        return jsonify({'error': error}), 400
    return jsonify(user.to_dict()), 201

@users_bp.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    data = request.get_json()
    user, error = update_user(user_id, data)
    if error == 'User not found':
        return jsonify({'error': error}), 404
    if error:
        return jsonify({'error': error}), 400
    return jsonify(user.to_dict()), 200