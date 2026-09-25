import pytest
from app import db
from app.models import User

def test_get_statistics_empty_db(client):
    res = client.get('/users/statistics')
    assert res.status_code == 200
    assert res.json['data']['total_users'] == 0

def test_get_statistics_logic(client):
    db.session.add(User(name='A', status='active', occupation='Dev', password='pass'))
    db.session.add(User(name='B', status='inactive', occupation=None, password='pass'))
    db.session.commit()
    res = client.get('/users/statistics')
    data = res.json['data']
    assert data['total_users'] == 2
    assert data['active_users'] == 1
    assert data['inactive_users'] == 1
    assert data['users_by_occupation']['Dev'] == 1
    assert data['users_by_occupation']['Unknown'] == 1
    assert 'password' not in str(res.json)