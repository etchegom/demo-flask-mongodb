from commands import user_cli
from typing import Generator, Iterable

import click
from omdb_fixtures_loader import loader
from pymongo import InsertOne, MongoClient

import settings

client = MongoClient(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
coll = client[settings.MONGODB_DB][settings.MONGODB_COLL]


def do_search(
    api_key: str, search: str, media_type: str
) -> Generator[dict, None, None]:
    """Perform a search on OMDB API

    Arguments:
        api_key {str} -- API key
        search {str} -- the text to search
        media_type {str} -- type of media

    Returns:
        Generator[dict, None, None] -- the search hits
    """
    for hit in loader.search_and_fetch(
        api_key=api_key, search=search, media_type=media_type
    ):
        yield hit


def save_to_db(hits: Iterable[dict]) -> int:
    """Save hits to database

    Arguments:
        hits {Iterable[dict]} -- List of hits

    Returns:
        int -- The number of hits that were saved
    """
    counter = 0

    reqs = []
    for hit in hits:
        reqs.append(InsertOne(hit))
        if len(reqs) > settings.MONGODB_BULK_SIZE - 1:
            res = coll.bulk_write(reqs)
            counter += res.inserted_count
    if len(reqs):
        res = coll.bulk_write(reqs)
        counter += res.inserted_count

    return counter


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
def populate(api_key: str, search: str, media_type: str, reset: bool) -> None:
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
        print("dropping collection {}".format(coll.name))
        coll.drop()

    count = save_to_db(
        hits=do_search(api_key=api_key, search=search, media_type=media_type)
    )
    print("{} items saved to database".format(count))
