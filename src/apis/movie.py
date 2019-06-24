from flask_restplus import Namespace, Resource, fields
from models import MovieDocument

api = Namespace("movies", description="Movies API")


movie_model = api.model("Movie", {"title": fields.String})


@api.route("/")
class MovieList(Resource):
    @api.marshal_with(movie_model, as_list=True, envelope="data")
    def get(self):
        return MovieDocument.objects.only("title").paginate(page=1, per_page=2).items
