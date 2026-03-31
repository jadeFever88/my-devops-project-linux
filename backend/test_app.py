import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_status(client):
    """Перевірка, що сервер повертає код 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Перевірка, що на сторінці є слово 'Успіх' або 'Помилка'"""
    response = client.get('/')
    # Ми перевіряємо байти (b''), бо Flask повертає дані в такому форматі
    assert b'\xd0\xa3\xd1\x81\xd0\xbf\xd1\x96\xd1\x85' in response.data or b'\xd0\x9f\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xba\xd0\xb0' in response.data
