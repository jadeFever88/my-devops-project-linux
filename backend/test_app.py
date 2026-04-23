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
    """Перевірка, що додаток повертає метрики у форматі Prometheus"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'hits_total' in response.data
    assert b'app_up' in response.data
