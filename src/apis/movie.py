from typing import List

from flask_paginate import get_page_args
from flask_restplus import Namespace, Resource, fields

from models import MovieDocument

api = Namespace("movies", description="Movies API")


movie_model = api.model("Movie", model={"title": fields.String})


@api.route("/")
class MovieList(Resource):
    @api.marshal_with(movie_model, as_list=True, envelope="data")
    def get(self) -> List[object]:
        page, per_page, _ = get_page_args(
            page_parameter="page", per_page_parameter="size"
        )
        return (
            MovieDocument.objects.only("title")
            .paginate(page=page, per_page=per_page)
            .items
        )
