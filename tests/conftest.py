import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    os.environ["PRIVATE_KEY"] = "a" * 64  # dummy 32-byte hex key for tests
    with TestClient(app) as c:
        yield c
