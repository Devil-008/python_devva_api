from app.models import db, User
from sqlalchemy import func

class UserService:
    @staticmethod
    def get_user_statistics():
        total = db.session.query(func.count(User.id)).scalar() or 0
        active = db.session.query(func.count(User.id)).filter(User.status == 'active').scalar() or 0
        inactive = db.session.query(func.count(User.id)).filter(User.status == 'inactive').scalar() or 0
        
        occupation_data = db.session.query(User.occupation, func.count(User.id)).group_by(User.occupation).all()
        occ_map = {}
        for occ, count in occupation_data:
            label = occ if occ and occ.strip() != '' else 'Unknown'
            occ_map[label] = occ_map.get(label, 0) + count

        return {
            "total_users": total,
            "active_users": active,
            "inactive_users": inactive,
            "users_by_occupation": occ_map
        }