import pytest
from jose import jwt
from app import schemas
from app.config import settings



def test_create_user(client):
    response = client.post("/users/", json={"email": "test@test.com", "password": "test123"})
    new_user = schemas.UserOut(**response.json())
    assert response.status_code ==  201
    assert new_user.email == "test@test.com"

def test_login_user(client, test_user):
    response = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_response.token_type == "bearer"
    assert response.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("abc@123.com", "test123", 403), # wrong email
    ("test@test.com", "asdf123", 403), # wrong password
    ("abc@123.com", "asdf123", 403), # wrong email and password
    (None, "test123", 422), # no email
    ("test@test.com", None, 422)]) # no password
def test_incorrect_login(client, email, password, status_code):
    response = client.post("/login", data={"username": email, "password": password})
    assert response.status_code == status_code
    