from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["POST"], strict_slashes=False)
def create_user():
    """
    POST /users
    Register/create a new user.
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Request payload must be valid JSON"}), 400

    user, error = UserService.create_user(data)
    if error:
        status_code = 409 if "already exists" in error else 400
        return jsonify({"error": error}), status_code

    return jsonify(user.to_dict()), 201


@users_bp.route("", methods=["GET"], strict_slashes=False)
def get_users():
    """
    GET /users
    Retrieve all users.
    """
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    """
    GET /users/<id>
    Retrieve a single user by ID.
    """
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    return jsonify(user.to_dict()), 200


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    """
    DELETE /users/<id>
    Delete a user by ID.
    """
    success = UserService.delete_user(user_id)
    if not success:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200
