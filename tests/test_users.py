import pytest
from app.models import User

def test_patch_user_success(client, init_database):
    user = User(name="Old", email="old@test.com")
    user.set_password("password123")
    # ... database logic omitted for brevity ...
    response = client.patch(f'/users/1', json={'name': 'New Name'})
    assert response.status_code == 200
    assert response.json['name'] == 'New Name'

def test_patch_user_invalid_email(client, init_database):
    response = client.patch('/users/1', json={'email': 'invalid-email'})
    assert response.status_code == 400

def test_patch_user_not_found(client):
    response = client.patch('/users/999', json={'name': 'New'})
    assert response.status_code == 404

def test_patch_password_exclusion(client, init_database):
    response = client.patch('/users/1', json={'name': 'Test'})
    assert 'password' not in response.json
    assert 'password_hash' not in response.json