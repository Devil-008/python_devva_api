import pytest
from app.models import User
def test_create_user(client):
    response = client.post('/users', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['id'] is not None
def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
def test_get_user(client):
    user = User(name='Test User', email='test@example.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    response = client.get(f'/users/{user.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == user.id
def test_delete_user(client):
    user = User(name='Test User', email='test@example.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    response = client.delete(f'/users/{user.id}')
    assert response.status_code == 204
def test_search_users(client):
    response = client.get('/users/search?q=test')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    response = client.get('/users/search?')
    assert response.status_code == 400
    response = client.get('/users/search?q=')
    assert response.status_code == 400