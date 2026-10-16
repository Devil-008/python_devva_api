from app.extensions import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'income' or 'expense'
    color = db.Column(db.String(7), nullable=True)     # Hex code e.g. #FF5733
    icon = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # Null means system category
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    transactions = db.relationship('Transaction', backref='category', lazy=True)

    def to_dict(self, current_user_id=None):
        from app.models.transaction import Transaction
        count = 0
        if current_user_id is not None:
            count = Transaction.query.filter_by(category_id=self.id, user_id=current_user_id).count()
        else:
            count = len(self.transactions)

        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "color": self.color,
            "icon": self.icon,
            "user_id": self.user_id,
            "is_system": self.user_id is None,
            "transaction_count": count,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
