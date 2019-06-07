from mongoengine import Document, StringField


class Movie(Document):
    title = StringField(max_length=255, required=True)
