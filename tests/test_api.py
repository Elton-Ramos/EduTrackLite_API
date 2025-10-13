from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ---------- USER TESTS ----------
def test_create_user():
    response = client.post("/users/", json={
        "name": "Dave",
        "email": "dave@example.com"
    })
    assert response.status_code == 201  # fixed indentation and updated code
    data = response.json()
    assert data["name"] == "Dave"
    assert data["email"] == "dave@example.com"


def test_create_course():
    response = client.post("/courses/", json={
        "title": "Math 101",
        "description": "Intro to Math"
    })
    assert response.status_code == 201  # fixed indentation and updated code
    data = response.json()
    assert data["title"] == "Math 101"


def test_create_enrollment():
    response = client.post("/enrollments/", json={
        "user_id": 1,
        "course_id": 1
    })
    assert response.status_code == 201  # fixed indentation and updated code
    data = response.json()
    assert data["user_id"] == 1
    assert data["course_id"] == 1
