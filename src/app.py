from flask import Flask

from apis import blueprint
from models import db
from populate import command as populate_command


def create_app(with_commands: bool = False) -> Flask:
    app = Flask(__name__)
    app.config.from_object("settings")
    db.init_app(app)
    app.register_blueprint(blueprint)

    if with_commands:
        app.cli.add_command(populate_command)

    return app


if __name__ == "__main__":
    app = create_app(with_commands=True)
    app.run(debug=True)
