from flask_admin.contrib.mongoengine import ModelView


class MovieDocumentView(ModelView):
    column_filters = ["title"]
    column_searchable_list = ("title",)
