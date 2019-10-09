from test_app import client  # noqa


def test_get_movies(client):  # noqa
    resp = client.get("/api/movies/")
    assert resp.status_code == 200
    assert len(resp.json.get("data")) == 0
