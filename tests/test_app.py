from http import HTTPStatus


def test_read_root_must_return_ok_and_hello_world(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (garante retorno)
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Validar se retornou o status code correto
    assert response.status_code == HTTPStatus.CREATED

    # Validar o UserPublic (Model/Schema)
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
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
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

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_update_user_exception(client):
    response = client.put(
        '/users/-1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': -1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_delete_user_exception(client):
    response = client.delete('/users/-1')

    assert response.status_code == HTTPStatus.NOT_FOUND
