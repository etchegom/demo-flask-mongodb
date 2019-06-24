import settings
from flask_mongoengine import MongoEngine

db = MongoEngine()


class MovieDocument(db.Document):
    meta = {"collection": settings.MONGODB_COLL}
    title = db.StringField()
