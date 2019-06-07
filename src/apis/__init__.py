from flask import Blueprint

from flask_restplus import Api
from apis.movie import api as api_movie

bp_api = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp_api, title="My Title", version="1.0", description="A description")
api.add_namespace(api_movie)
