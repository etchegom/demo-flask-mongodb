import click
from flask import Flask
from flask.cli import AppGroup
from flask_debugtoolbar import DebugToolbarExtension

import populate
from apis import blueprint
from models import db

dev_cli = AppGroup("dev", help="Dev")


@dev_cli.command("populate")
@click.option(
    "-k", "--apikey", "api_key", required=True, prompt=True, help="OMDB api key"
)
@click.option(
    "-s",
    "--search",
    default="starwars",
    required=False,
    help="Text to search in OMDB search request",
)
@click.option(
    "-t",
    "--type",
    "media_type",
    type=click.Choice(["movie", "episode", "series"], case_sensitive=False),
    required=False,
    help="Type of media to search",
)
@click.option("-r", "--reset", is_flag=True, help="Reset database before populating")
def populate_db(api_key: str, search: str, media_type: str, reset: bool) -> None:
    """Populate database with data fetched from the OMDB API

    Arguments:
        api_key {str} -- API key
        search {str} -- the text to search
        media_type {str} -- type of media
        reset {bool} -- reset database before populate (drop mongodb collection)

    Returns:
        None -- [description]
    """
    if reset:
        populate.reset()

    count = populate.save_to_db(
        hits=populate.do_search(api_key=api_key, search=search, media_type=media_type)
    )
    print("{} items saved to database".format(count))


def create_app(**config_overrides: dict) -> Flask:
    """Create the Flask app

    Returns:
        Flask -- a Flask app instance
    """

    app = Flask(__name__)

    # setup app config
    app.config.from_object("settings")
    app.config.update(config_overrides)

    # setup database
    db.init_app(app)

    # setup blueprints
    app.register_blueprint(blueprint)

    # setup CLI commands
    app.cli.add_command(dev_cli)

    # setup debug toolbar
    app.config["DEBUG_TB_PANELS"] = ["flask_mongoengine.panels.MongoDebugPanel"]
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
