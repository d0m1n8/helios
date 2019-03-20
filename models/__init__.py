from pymongo import MongoClient
from configs import config

def mongo_connection():
    mongo_url = config.Config.MONGODB_URI
    helios_client = MongoClient(mongo_url)
    return helios_client.get_database()
