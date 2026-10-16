from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app import db
from app.models.category import Category
import re

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/api/v1/categories', methods=['POST'])
@login_required
def create_category():
    data = request.get_json()
    if data.get('type') not in ['income', 'expense']:
        return {'error': 'Invalid type'}, 400
    if not re.match(r'^#([A-Fa-f0-9]{6})$', data.get('color', '')):
        return {'error': 'Invalid color format'}, 400
    if Category.query.filter_by(user_id=current_user.id, name=data['name'], type=data['type']).first():
        return {'error': 'Name must be unique for this type'}, 400
    new_cat = Category(name=data['name'], type=data['type'], color=data['color'], icon=data['icon'], user_id=current_user.id)
    db.session.add(new_cat)
    db.session.commit()
    return new_cat.to_dict(current_user.id), 201

@categories_bp.route('/api/v1/categories/<int:id>', methods=['PUT'])
@login_required
def update_category(id):
    cat = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    data = request.get_json()
    cat.name = data.get('name', cat.name)
    cat.color = data.get('color', cat.color)
    cat.icon = data.get('icon', cat.icon)
    db.session.commit()
    return cat.to_dict(current_user.id), 200

@categories_bp.route('/api/v1/categories/<int:id>', methods=['DELETE'])
@login_required
def delete_category(id):
    cat = Category.query.get_or_404(id)
    if cat.user_id is None:
        return {'error': 'System categories cannot be deleted'}, 403
    count = cat.to_dict(current_user.id).get('transaction_count', 0)
    if count > 0:
        return {'error': f'Cannot delete category associated with {count} existing transactions.', 'transaction_count': count}, 400
    db.session.delete(cat)
    db.session.commit()
    return '', 204