from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero_course.app import app


def test_read_root_must_return_ok_and_hello_world():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (garante retorno)
    assert response.json() == {
        'message': 'Minha namorada é a mais linda do mundo!'
    }
