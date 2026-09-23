import pytest
from app.models import User
from app.extensions import db

def test_update_profile_success(client):
    user = User(name='Test', email='test@test.com', password='pwd')
    db.session.add(user)
    db.session.commit()
    response = client.patch(f'/users/{user.id}/profile', json={'occupation': 'Dev'})
    assert response.status_code == 200
    assert response.get_json()['occupation'] == 'Dev'

def test_update_profile_invalid_date(client):
    user = User(name='Test', email='t@t.com', password='p')
    db.session.add(user)
    db.session.commit()
    response = client.patch(f'/users/{user.id}/profile', json={'date_of_birth': 'invalid'})
    assert response.status_code == 400

def test_update_nonexistent_user(client):
    response = client.patch('/users/999/profile', json={'occupation': 'New'})
    assert response.status_code == 404

def test_password_not_in_response(client):
    user = User(name='Test', email='p@p.com', password='pwd')
    db.session.add(user)
    db.session.commit()
    response = client.patch(f'/users/{user.id}/profile', json={'occupation': 'Dev'})
    data = response.get_json()
    assert 'password' not in data