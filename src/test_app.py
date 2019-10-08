import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.debug = True
    app.config["TESTING"] = True
    yield app.test_client()


def test_dummy(client):
    resp = client.get("/dummy")
    assert resp.status_code == 404
