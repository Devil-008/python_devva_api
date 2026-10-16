import pytest
from app.models.user import User, db

def test_update_profile_success(client, auth_headers):
    response = client.put('/api/v1/auth/profile', json={
        'name': 'Alex Doe',
        'currency': 'USD',
        'theme': 'dark'
    }, headers=auth_headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Profile updated successfully.'
    assert data['user']['name'] == 'Alex Doe'
    assert data['user']['currency'] == 'USD'
    assert data['user']['theme'] == 'dark'

def test_update_profile_invalid_currency(client, auth_headers):
    response = client.put('/api/v1/auth/profile', json={
        'currency': 'XYZ'
    }, headers=auth_headers)
    assert response.status_code == 400
    assert 'Unsupported currency code' in response.get_json()['error']

def test_update_profile_invalid_name(client, auth_headers):
    response = client.put('/api/v1/auth/profile', json={
        'name': ''
    }, headers=auth_headers)
    assert response.status_code == 400
    assert 'Name must be between' in response.get_json()['error']
