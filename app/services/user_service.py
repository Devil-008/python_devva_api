import math
from app.models import User, db

class UserService:
    @staticmethod
    def get_all_users(page=1, limit=10, sort_by='created_at', order='desc'):
        if page < 1 or limit < 1:
            return None, "Invalid page or limit"
        
        valid_sorts = ['name', 'email', 'created_at']
        if sort_by not in valid_sorts:
            return None, "Invalid sort field"
        
        if order not in ['asc', 'desc']:
            return None, "Invalid order"

        query = User.query
        query = query.order_by(getattr(User, sort_by).asc() if order == 'asc' else getattr(User, sort_by).desc())
        
        total = query.count()
        total_pages = math.ceil(total / limit) if total > 0 else 0
        users = query.offset((page - 1) * limit).limit(limit).all()
        
        return {
            "users": [{k: v for k, v in u.to_dict().items() if k != 'password'} for u in users],
            "current_page": page,
            "page_size": limit,
            "total_users": total,
            "total_pages": total_pages
        }, None