import click
from flask import Flask

import populate
from apis import blueprint
from models import db

app = Flask(__name__)
app.config.from_object("settings")
db.init_app(app)
app.register_blueprint(blueprint)


@app.cli.command("populate")
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
def populate_command(api_key: str, search: str, media_type: str, reset: bool) -> None:
    populate.do_work(api_key, search, media_type, reset)


if __name__ == "__main__":
    app.run(debug=True)
