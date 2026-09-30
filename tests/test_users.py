import pytest
from app import create_app, db
from app.models import User

def test_get_users_default_pagination(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()['data']
    assert 'users' in data
    assert data['current_page'] == 1

def test_get_users_invalid_params(client):
    assert client.get('/users?page=0').status_code == 400
    assert client.get('/users?limit=-1').status_code == 400
    assert client.get('/users?sort_by=invalid').status_code == 400

def test_get_users_sorting(client):
    response = client.get('/users?sort_by=name&order=asc')
    assert response.status_code == 200

def test_get_users_password_exclusion(client):
    response = client.get('/users')
    users = response.get_json()['data']['users']
    for user in users:
        assert 'password' not in user

def test_get_users_combined_pagination_sorting(client):
    response = client.get('/users?page=1&limit=5&sort_by=email&order=desc')
    assert response.status_code == 200
    data = response.get_json()['data']
    assert data['page_size'] == 5