from flask import Blueprint
from flask_restplus import Api

from apis.movie import api as api_movie

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, title="My Title", version="1.0", description="A description")
api.add_namespace(api_movie)
