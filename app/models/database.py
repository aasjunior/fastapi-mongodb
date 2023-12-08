from pymongo import MongoClient
from app.settings import Settings

settings = Settings()

client = MongoClient(settings.MONGODB_URL)
db = client.get_database(settings.DB_NAME)
collection = db["collection"]
