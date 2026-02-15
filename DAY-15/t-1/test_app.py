import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = User(username="admin", password="1234")
            db.session.add(user)
            db.session.commit()
        yield client

def test_login_success(client):
    response = client.post("/login", data={"username": "admin", "password": "1234"})
    assert b"Welcome, admin!" in response.data

def test_login_failure(client):
    response = client.post("/login", data={"username": "wrong", "password": "wrong"})
    assert b"Invalid credentials" in response.data