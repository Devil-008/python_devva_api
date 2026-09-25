from flask import Blueprint
from app.controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['POST'])(UserController.create_user)
user_bp.route('/', methods=['GET'])(UserController.get_all_users)
user_bp.route('/<int:user_id>', methods=['GET'])(UserController.get_user_by_id)
user_bp.route('/<int:user_id>', methods=['DELETE'])(UserController.delete_user)
user_bp.route('/<int:user_id>/profile', methods=['PUT', 'PATCH'])(UserController.update_user_profile)
user_bp.route('/filter', methods=['GET'])(UserController.filter_users)
user_bp.route('/statistics', methods=['GET'])(UserController.get_statistics)