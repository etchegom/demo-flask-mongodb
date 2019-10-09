import factory
import mongoengine
import pytest
from app import create_app
from models import MovieDocument


@pytest.fixture
def client():
    app = create_app(MONGODB_SETTINGS={"DB": "test"}, TESTING=True)
    app.debug = True
    assert app.config["TESTING"]

    db = mongoengine.connection.get_db()
    assert db.name == "test"

    yield app.test_client()

    conn = mongoengine.connection.get_connection()
    conn.drop_database("test")


class MovieDocumentFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = MovieDocument

    title = factory.Sequence(lambda n: "title %d" % n)
