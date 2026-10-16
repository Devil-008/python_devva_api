from app import db
from app.models.transaction import Transaction

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(7), default='#FFFFFF')
    icon = db.Column(db.String(50), default='shopping')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def to_dict(self, current_user_id=None):
        transaction_count = Transaction.query.filter_by(category_id=self.id).count() if current_user_id else 0
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'color': self.color,
            'icon': self.icon,
            'is_system': self.user_id is None,
            'transaction_count': transaction_count
        }