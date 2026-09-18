import re
from app.models import User
from app.extensions import db

def create_user(name, email, password):
    if not name or not email or not password:
        return None, "Missing fields"
    if User.query.filter_by(email=email).first():
        return None, "User with this email already exists"
    user = User(name=name.strip(), email=email.strip())
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
        if not isinstance(email, str) or not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return None, "Invalid email format"
        if User.query.filter(User.email == email.strip(), User.id != user_id).first():
            return None, "Email already in use"
        user.email = email.strip()

    if 'password' in data:
        password = data['password']
        if not isinstance(password, str) or len(password) < 8:
            return None, "Password must be at least 8 characters long"
        user.set_password(password)

    db.session.commit()
    return user, None