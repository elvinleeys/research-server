import pytest
from fastapi.testclient import TestClient
from app.main import app
from pathlib import Path


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_files_dir():
    return Path(__file__).parent / "files"