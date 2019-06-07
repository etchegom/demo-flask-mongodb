from flask import Flask

from apis import bp_api
from db_engine import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("settings")

    db.init_app(app)

    app.register_blueprint(bp_api)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
