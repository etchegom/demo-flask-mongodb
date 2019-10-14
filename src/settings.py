import os

SECRET_KEY = "my secret key"

MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGODB_PORT = int(os.getenv("MONGODB_PORT", "27017"))
MONGODB_DB = os.getenv("MONGODB_DB", "demo")
MONGODB_COLL = os.getenv("MONGODB_COLL", "movie")
MONGODB_BULK_SIZE = int(os.getenv("MONGODB_BULK_SIZE", "100"))
