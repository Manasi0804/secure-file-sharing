from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Shared emails for client & ops
client_email = "testclient@example.com"
ops_email = "testops@example.com"

def test_1_signup_client():
    response = client.post("/auth/signup/client", json={
        "email": client_email,
        "password": "client123",
        "role": "client"
    })
    assert response.status_code in [200, 400]  # 400 if user exists

def test_2_login_client():
    response = client.post("/auth/login", json={
        "email": client_email,
        "password": "client123",
        "role": "client"
    })
    assert response.status_code == 200
    assert "token" in response.json()

def test_3_login_ops_fail():
    # This ops user doesn’t exist yet
    response = client.post("/auth/login", json={
        "email": ops_email,
        "password": "ops123",
        "role": "ops"
    })
    assert response.status_code == 401 or response.status_code == 500

def test_4_list_files_without_token():
    response = client.get("/client/list-files")
    assert response.status_code == 401  # Should require auth

def test_5_upload_without_token():
    with open("tests/sample.docx", "wb") as f:
        f.write(b"Test Word File")  # create a dummy file
    with open("tests/sample.docx", "rb") as f:
        response = client.post("/ops/upload", files={"file": f})
    assert response.status_code == 401  # Unauthorized
