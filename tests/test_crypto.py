import base64
import json

def test_encrypt_decrypt_basic_json(client):
    payload = {"name": "John", "age": 42}
    encrypt_response = client.post("/api/v1/crypto/encrypt", json=payload)
    assert encrypt_response.status_code == 200
    encrypted_data = encrypt_response.json()
    decrypt_response = client.post("/api/v1/crypto/decrypt", json=encrypted_data)
    assert decrypt_response.status_code == 200
    decrypted_data = decrypt_response.json()
    assert decrypted_data == payload

def test_sign_returns_signature(client):
    payload = {"name": "John", "age": 42}
    response = client.post("/api/v1/crypto/sign", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "signature" in data
    assert isinstance(data["signature"], str)
    assert len(data["signature"]) == 64  # SHA256 hex digest

def test_verify_valid_signature(client):
    payload = {"name": "John", "age": 42}
    sign_response = client.post("/api/v1/crypto/sign", json=payload)
    assert sign_response.status_code == 200
    signature = sign_response.json()["signature"]
    payload["signature"] = signature
    verify_response = client.post("/api/v1/crypto/verify", json=payload)
    assert verify_response.status_code == 204

def test_verify_invalid_signature(client):
    payload = {
        "name": "John",
        "age": 42,
        "signature": "invalid" * 8
    }
    response = client.post("/api/v1/crypto/verify", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Signature is invalid"

def test_encrypt_invalid_payload(client):
    response = client.post("/api/v1/crypto/encrypt", content="not a json")
    assert response.status_code == 422  # Unprocessable Entity

def test_decrypt_malformed_base64(client):
    payload = {"bad": "@@@@"}
    response = client.post("/api/v1/crypto/decrypt", json=payload)
    assert response.status_code == 200  # Still 200, returns error in value
    assert "error" not in response.json()

def test_verify_missing_signature(client):
    payload = {"name": "Alice"}
    response = client.post("/api/v1/crypto/verify", json=payload)
    assert response.status_code == 422
