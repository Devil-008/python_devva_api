import re
from typing import List, Optional, Tuple
from app.extensions import db
from app.models import User
from app.extensions import db

def validate_email(email):
    return re.match(r"^[^@]+@[^@]+\.[^@]+", email) is not None

def create_user(name, email, password):
    if not name or not isinstance(name, str) or not name.strip():
        return None, "Field 'name' is required"
    if not email or not isinstance(email, str) or not email.strip():
        return None, "Field 'email' is required"
    if not password or not isinstance(password, str) or not password.strip():
        return None, "Field 'password' is required"

    email_clean = email.strip()
    if not validate_email(email_clean):
        return None, "Invalid email format"

    existing_user = User.query.filter_by(email=email_clean).first()
    if existing_user:
        return None, "User with this email already exists"

    user = User(name=name.strip(), email=email_clean)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user, None

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None, "User not found"

    if 'name' in data:
        name = data['name']
        if not isinstance(name, str) or not name.strip():
            return None, "Name cannot be empty"
        user.name = name.strip()

    if 'email' in data:
        email = data['email']
        if not isinstance(email, str) or not validate_email(email.strip()):
            return None, "Invalid email format"
        email_clean = email.strip()
        existing = User.query.filter(User.email == email_clean, User.id != user_id).first()
        if existing:
            return None, "Email already in use"
        user.email = email_clean

    if 'password' in data:
        pwd = data['password']
        if not isinstance(pwd, str) or len(pwd) < 6:
            return None, "Password must be at least 6 characters long"
        user.set_password(pwd)

    db.session.commit()
    return user, None

class UserService:
    """Service class handling business logic for User entity."""

    @staticmethod
    def create_user(data: dict) -> Tuple[Optional[User], Optional[str]]:
        """
        Create a new user.

        Validates presence of required fields (name, email, password),
        checks email format via regex, and checks for duplicate email addresses.
        """
        if not data:
            return None, "Request body must be valid JSON"

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not isinstance(name, str) or not name.strip():
            return None, "Field 'name' is required"

        if not email or not isinstance(email, str) or not email.strip():
            return None, "Field 'email' is required"

        if not password or not isinstance(password, str) or not password.strip():
            return None, "Field 'password' is required"

        email_clean = email.strip()
        
        # Email format validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email_clean):
            return None, "Invalid email format"

        # Check if email is already registered
        existing_user = User.query.filter_by(email=email_clean).first()
        if existing_user:
            return None, "User with this email already exists"

        # Instantiate user and hash password
        user = User(name=name.strip(), email=email_clean)
        user.set_password(password)

        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception as e:
            db.session.rollback()
            return None, f"Failed to create user: {str(e)}"

    @staticmethod
    def get_all_users() -> List[User]:
        """Fetch all users from database."""
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Fetch a single user by primary key ID."""
        return db.session.get(User, user_id)

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Delete a user by primary key ID."""
        user = db.session.get(User, user_id)
        if not user:
            return False

        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False
