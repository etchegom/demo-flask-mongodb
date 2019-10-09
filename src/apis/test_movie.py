def test_get_movies(client):
    resp = client.get("/api/movies")
    assert resp.status_code == 200
