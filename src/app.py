from commands import user_cli

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from apis import blueprint
from models import db


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
        app.cli.add_command(user_cli)

    # setup debug toolbar
    app.config["DEBUG_TB_PANELS"] = ["flask_mongoengine.panels.MongoDebugPanel"]
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app(with_commands=True)
    app.run(debug=True)
