from flask import Flask

from apis import blueprint
from models import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("settings")

    db.init_app(app)

    app.register_blueprint(blueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
