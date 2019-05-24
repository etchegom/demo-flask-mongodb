if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("apikey", help="OMDB API key", type=str)
    args = parser.parse_args()

    print(args)

# http --json "http://www.omdbapi.com/?apikey=eb88cc&r=json&type=movie&s=star+wars"
# http --json "http://www.omdbapi.com/?apikey=eb88cc&r=json&type=movie&s=avengers"
# http --json "http://www.omdbapi.com/?apikey=eb88cc&r=json&i=tt2395427"
