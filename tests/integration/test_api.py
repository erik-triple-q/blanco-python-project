# tests/integration/test_api.py
"""Integration tests for FastAPI presentation endpoints using TestClient."""

from fastapi.testclient import TestClient


def test_health_check_returns_200_and_healthy_status(client: TestClient) -> None:
    # Arrange & Act
    response = client.get("/health")

    # Assert
    assert response.status_code == 200 and response.json()["status"] == "healthy"


def test_create_item_returns_201_and_item_payload(client: TestClient) -> None:
    # Arrange
    payload = {"title": "API Item", "description": "Created via API"}

    # Act
    response = client.post("/api/v1/items", json=payload)

    # Assert
    assert response.status_code == 201 and response.json()["title"] == "API Item"


def test_get_item_with_unknown_id_returns_404(client: TestClient) -> None:
    # Arrange & Act
    response = client.get("/api/v1/items/non-existent-uuid")

    # Assert
    assert response.status_code == 404


def test_activate_item_endpoint_transitions_status(client: TestClient) -> None:
    # Arrange
    create_resp = client.post(
        "/api/v1/items",
        json={"title": "Draft to Activate", "description": ""},
    )
    item_id = create_resp.json()["id"]

    # Act
    activate_resp = client.post(f"/api/v1/items/{item_id}/activate")

    # Assert
    assert activate_resp.status_code == 200 and activate_resp.json()["status"] == "active"


def test_delete_item_endpoint_returns_204(client: TestClient) -> None:
    # Arrange
    create_resp = client.post("/api/v1/items", json={"title": "To Delete"})
    item_id = create_resp.json()["id"]

    # Act
    del_resp = client.delete(f"/api/v1/items/{item_id}")

    # Assert
    assert del_resp.status_code == 204
