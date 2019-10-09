from flask import Flask

from apis import blueprint
from models import db
from populate import command as populate_command


def create_app(with_commands: bool = False, **config_overrides: dict) -> Flask:
    app = Flask(__name__)

    # setup app config
    app.config.from_object("settings")
    app.config.update(config_overrides)

    # setup database
    db.init_app(app)

    # setup blueprints
    app.register_blueprint(blueprint)

    # setup CLI commands
    if with_commands:
        app.cli.add_command(populate_command)

    return app


if __name__ == "__main__":
    app = create_app(with_commands=True)
    app.run(debug=True)
