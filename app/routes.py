from flask import request, jsonify
from app import app
from app.services.user_service import create_user, update_user

@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    user, error = create_user(data.get('name'), data.get('email'), data.get('password'))
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user_route(user_id):
    data = request.get_json()
    user, error = update_user(user_id, data)
    if error:
        status = 404 if error == "User not found" else 400
        return jsonify({"error": error}), status
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200