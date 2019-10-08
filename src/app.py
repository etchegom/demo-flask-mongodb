from flask import Flask

from apis import blueprint
from models import db
from populate import command as populate_command


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    db.init_app(app)
    app.register_blueprint(blueprint)
    app.cli.add_command(populate_command)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
