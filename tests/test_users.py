import pytest

def test_create_user_valid(client):
    response = client.post('/users', json={'name': 'Jane Doe', 'email': 'jane@example.com', 'password': 'secretpassword'})
    assert response.status_code == 201
    assert response.json['email'] == 'jane@example.com'

def test_create_user_invalid_email(client):
    invalid_emails = ['john', 'john@', '@example.com', 'john@example', 'john example@gmail.com']
    for email in invalid_emails:
        response = client.post('/users', json={'name': 'Test', 'email': email, 'password': 'pw'})
        assert response.status_code == 400
        assert response.json['error'] == 'Invalid email format'

def test_create_user_missing_email(client):
    response = client.post('/users', json={'name': 'Test', 'password': 'pw'})
    assert response.status_code == 400
    assert response.json['error'] == "Field 'email' is required"

def test_existing_functionality_preserved(client):
    # Ensure users can still be listed
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)