# typing: ignore

from test_app import client  # noqa
from test_app import MovieDocumentFactory


def test_get_movies(client):  # noqa
    movie_a = MovieDocumentFactory(title=u"quatre garçons plein d'avenir")
    movie_b = MovieDocumentFactory(title=u"les tontons flingueurs")

    resp = client.get("/api/movies/")
    assert resp.status_code == 200

    data = resp.json.get("data")
    assert data == [{"title": movie_b.title}, {"title": movie_a.title}]
