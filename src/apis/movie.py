from flask_restplus import Namespace, Resource, fields
from models.movie import Movie

api = Namespace("movies", description="Movies API")

movie_schema = api.schema_model(
    "Movie",
    schema={"type": "object", "required": ["title"], "properties": {"title": "string"}},
)

movie_model = api.model("Movie", {"title": fields.String})


@api.route("/")
class MovieList(Resource):
    @api.marshal_list_with(movie_model)
    def get(self):
        return Movie.objects().only("title")
