from typing import List, Optional, Tuple
from app.extensions import db
from app.models import User
class UserService:
    """Service class handling business logic for User entity.""
    @staticmethod
def create_user(data: dict) -> Tuple[Optional[User], Optional[str]]:
        if not data:
            return None, 'Request body must be valid JSON'
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not name or not isinstance(name, str) or not name.strip():
            return None, 'Field \'name\' is required'
        if not email or not isinstance(email, str) or not email.strip():
            return None, 'Field \'email\' is required'
        if not password or not isinstance(password, str) or not password.strip():
            return None, 'Field \'password\' is required'
        email_clean = email.strip()
        existing_user = User.query.filter_by(email=email_clean).first()
        if existing_user:
            return None, 'User with this email already exists'
        user = User(name=name.strip(), email=email_clean)
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)
    @staticmethod
def get_all_users() -> List[User]:
        return User.query.all()
    @staticmethod
def get_user_by_id(user_id: int) -> Optional[User]:
        return User.query.get(user_id)
    @staticmethod
def delete_user(user_id: int) -> bool:
        user = User.query.get(user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True
    @staticmethod
def search_users(q: str) -> List[User]:
        return User.query.filter((User.name.ilike(f'%{q}%')) | (User.email.ilike(f'%{q}%'))).all()