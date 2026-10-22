from flask import request, jsonify
from app.models import Transaction, db
import math

def get_transactions():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    q = request.args.get('q', '')
    sort_by = request.args.get('sort_by', 'transaction_date')
    sort_order = request.args.get('sort_order', 'desc')
    
    query = Transaction.query
    if q:
        query = query.filter(Transaction.note.ilike(f'%{q}%'))
    
    sort_attr = getattr(Transaction, sort_by, Transaction.transaction_date)
    query = query.order_by(sort_attr.desc() if sort_order == 'desc' else sort_attr.asc())
    
    total = query.count()
    transactions = query.offset((page - 1) * per_page).limit(per_page).all()
    
    return jsonify({
        "transactions": [t.to_dict() for t in transactions],
        "pagination": {
            "total_items": total,
            "total_pages": math.ceil(total / per_page) if per_page > 0 else 1,
            "current_page": page,
            "per_page": per_page,
            "has_next": page * per_page < total,
            "has_prev": page > 1
        }
    })