from typing import Generator, Iterable
from pymongo import MongoClient, InsertOne
import settings


client = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
coll = client[settings.MONGO_DB][settings.MONGO_COLL]


def search(api_key: str, search: str, media_type: str) -> Generator[dict, None, None]:
    """Perform a search on OMDB API

    Arguments:
        api_key {str} -- API key
        search {str} -- the text to search
        media_type {str} -- type of media

    Returns:
        Generator[dict, None, None] -- the search hits
    """
    for hit in loader.search_and_fetch(
        api_key=args.api_key, search=args.search, media_type=args.media_type
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
        if len(reqs) > settings.MONGO_BULK_SIZE - 1:
            res = coll.bulk_write(reqs)
            counter += res.inserted_count
    if len(reqs):
        res = coll.bulk_write(reqs)
        counter += res.inserted_count

    return counter


if __name__ == "__main__":
    import argparse
    from omdb_fixtures_loader import loader

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apikey", dest="api_key", required=True, help="Your OMDB API key"
    )
    parser.add_argument(
        "--search", dest="search", required=True, help="The text to search"
    )
    parser.add_argument(
        "--type", dest="media_type", required=False, help="Type of media"
    )
    parser.add_argument(
        "--reset",
        dest="reset",
        required=False,
        action="store_true",
        help="Reset database before pushing data",
    )
    args = parser.parse_args()

    if args.reset:
        coll.drop()

    count = save_to_db(
        hits=search(
            api_key=args.api_key, search=args.search, media_type=args.media_type
        )
    )
    print("{} items saved to database".format(count))
