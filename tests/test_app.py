from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_read_root_deve_retornar_ok(client):
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_html_endpoint(client):
    response = client.get('/html')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert


#    assert response.json() == {'message': 'Testes'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    # Validar UserPublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'testusername', 'email': 'test@test.com', 'id': 1}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }

    response = client.put(
        '/users/2',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 2,
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted!'}

    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
