from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.category import Category
from app.models.transaction import Transaction
import re

categories_bp = Blueprint('categories', __name__, url_prefix='/api/v1/categories')

@categories_bp.route('', methods=['GET'])
def get_categories():
    user_id = request.args.get('user_id', type=int)
    # Fetch system categories (user_id is None) and user-specific categories if user_id provided
    if user_id:
        categories = Category.query.filter((Category.user_id == None) | (Category.user_id == user_id)).all()
        return jsonify([c.to_dict(current_user_id=user_id) for c in categories]), 200
    else:
        categories = Category.query.all()
        return jsonify([c.to_dict() for c in categories]), 200

@categories_bp.route('', methods=['POST'])
def create_category():
    data = request.get_json() or {}
    name = data.get('name')
    cat_type = data.get('type')
    color = data.get('color')
    icon = data.get('icon')
    user_id = data.get('user_id')

    if not name or not cat_type:
        return jsonify({"error": "Name and type are required"}), 400

    if cat_type not in ['income', 'expense']:
        return jsonify({"error": "Type must be either 'income' or 'expense'"}), 400

    if color and not re.match(r'^#([A-Fa-f0-9]{6})$', color):
        return jsonify({"error": "Invalid color hex format. Use #RRGGBB"}), 400

    if user_id:
        existing = Category.query.filter_by(user_id=user_id, type=cat_type, name=name).first()
        if existing:
            return jsonify({"error": f"Category with name '{name}' already exists for this type."}), 400

    new_cat = Category(
        name=name,
        type=cat_type,
        color=color,
        icon=icon,
        user_id=user_id
    );
    db.session.add(new_cat)
    db.session.commit()

    return jsonify(new_cat.to_dict(current_user_id=user_id)), 201

@categories_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.get_json() or {}

    if category.user_id is None:
        return jsonify({"error": "System categories cannot be modified"}), 403

    name = data.get('name', category.name)
    cat_type = data.get('type', category.type)
    color = data.get('color', category.color)
    icon = data.get('icon', category.icon)
    user_id = category.user_id

    if cat_type not in ['income', 'expense']:
        return jsonify({"error": "Type must be either 'income' or 'expense'"}), 400

    if color and not re.match(r'^#([A-Fa-f0-9]{6})$', color):
        return jsonify({"error": "Invalid color hex format. Use #RRGGBB"}), 400

    if name != category.name or cat_type != category.type:
        existing = Category.query.filter_by(user_id=user_id, type=cat_type, name=name).first()
        if existing and existing.id != category.id:
            return jsonify({"error": f"Category with name '{name}' already exists for this type."}), 400

    category.name = name
    category.type = cat_type
    category.color = color
    category.icon = icon
    db.session.commit()

    return jsonify(category.to_dict(current_user_id=user_id)), 200

@categories_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    user_id = request.args.get('user_id', type=int)

    if category.user_id is None:
        return jsonify({"error": "System categories cannot be deleted"}), 403

    transaction_count = Transaction.query.filter_by(category_id=category.id).count()
    if transaction_count > 0:
        return jsonify({
            "error": f"Cannot delete category associated with {transaction_count} existing transactions. Reassign or delete transactions first.",
            "transaction_count": transaction_count
        }), 400

    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully"}), 200
