from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
users_bp = Blueprint('users', __name__)

@users_bp.route('', methods=['GET'], strict_slashes=False)
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': f'User with ID {user_id} not found'}), 404
    return jsonify(user.to_dict()), 200

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    success = UserService.delete_user(user_id)
    if not success:
        return jsonify({'error': f'User with ID {user_id} not found'}), 404
    return '', 204

@users_bp.route('/search', methods=['GET'], strict_slashes=False)
def search_users():
    q = request.args.get('q')
    if not q:
        return jsonify({'error': 'Missing search parameter'}), 400
    if not q.strip():
        return jsonify({'error': 'Search parameter cannot be empty or whitespace only'}), 400
    users = UserService.search_users(q)
    return jsonify([user.to_dict(exclude=['password']) for user in users]), 200