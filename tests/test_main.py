from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ---------- USER TESTS ----------
def test_create_user():
    response = client.post("/users/", json={
        "name": "Alice",
        "email": "alice@example.com",
        "is_active": True
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

# ---------- COURSE TESTS ----------
def test_create_course():
    response = client.post("/courses/", json={
        "title": "Python Basics",
        "description": "Learn Python",
        "is_open": True
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Python Basics"

def test_get_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ---------- ENROLLMENT TESTS ----------
def test_enroll_user():
    response = client.post("/enrollments/", json={
        "user_id": 1,
        "course_id": 1
    })
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["user_id"] == 1
    assert data["course_id"] == 1

def test_get_enrollments():
    response = client.get("/enrollments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
