import click
from flask.cli import AppGroup

import populate

user_cli = AppGroup("dev")


@user_cli.command("populate")
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
