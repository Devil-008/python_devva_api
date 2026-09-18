import re
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