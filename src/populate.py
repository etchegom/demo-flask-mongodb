if __name__ == "__main__":
    import argparse
    from pprint import pprint
    from omdb_fixtures_loader import loader

    parser = argparse.ArgumentParser()
    parser.add_argument("--apikey", dest="api_key", required=True, help="OMDB API key")
    parser.add_argument("--search", dest="search", required=True, help="The text to search")
    parser.add_argument("--type", dest="media_type", required=False, help="Type of media")
    args = parser.parse_args()

    for hit in loader.search_and_fetch(
        api_key=args.api_key, search=args.search, media_type=args.media_type
    ):
        pprint(hit)
