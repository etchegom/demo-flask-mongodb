import logging
from typing import Generator, Iterable

from omdb_fixtures_loader import loader
from omdb_fixtures_loader.loader import LoaderException
from pymongo import InsertOne, MongoClient

import settings

client = MongoClient(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
coll = client[settings.MONGODB_DB][settings.MONGODB_COLL]


logger = logging.getLogger(__name__)


def reset() -> None:
    print("dropping collection {}".format(coll.name))
    coll.drop()


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

    try:
        for hit in loader.search_and_fetch(
            api_key=api_key, search=search, media_type=media_type
        ):
            yield hit
    except LoaderException as e:
        logger.error(str(e))


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
