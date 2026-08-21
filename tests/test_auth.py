from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register():

    response = client.post(
        "/auth/register",
        json={
            "full_name": "Usuario Hospital",
            "email": "usuario_test@hospital.local",
            "password": "Password123",
            "role": "usuario"
        }
    )

    # Puede ser 201 si es nuevo
    # o 409 si ya existe

    assert response.status_code in [
        201,
        409
    ]


def test_login():

    response = client.post(
        "/auth/login",
        json={
            "email": "usuario_test@hospital.local",
            "password": "Password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data

    assert data["token_type"] == "bearer"