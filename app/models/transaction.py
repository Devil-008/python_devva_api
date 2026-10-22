from app.models import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    amount = db.Column(db.Float)
    transaction_date = db.Column(db.Date)
    payment_method = db.Column(db.String(50))
    note = db.Column(db.String(255))
    category = db.relationship('Category', backref='transactions')

    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else 'Uncategorized',
            'category_color': self.category.color if self.category else '#CBD5E1',
            'type': 'expense',
            'amount': self.amount,
            'transaction_date': self.transaction_date.isoformat(),
            'payment_method': self.payment_method,
            'note': self.note
        }