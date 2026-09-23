from app.models import User
from app.extensions import db
from datetime import datetime
import re

class UserService:
    @staticmethod
    def update_user_profile(user_id, data):
        user = User.query.get_or_404(user_id)
        
        if 'occupation' in data: user.occupation = data['occupation']
        if 'address' in data: user.address = data['address']
        
        if 'phone_number' in data:
            if not re.match(r'^\+?\d{10,15}$', data['phone_number']):
                raise ValueError("Invalid phone format")
            user.phone_number = data['phone_number']
            
        if 'date_of_birth' in data:
            try:
                user.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Invalid date format, expected YYYY-MM-DD")
        
        db.session.commit()
        return user.to_dict()