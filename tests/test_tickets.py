from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_tickets_requires_authentication():

    response = client.get(
        "/tickets"
    )

    assert response.status_code == 401