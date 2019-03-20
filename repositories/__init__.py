import os
from pymongo import MongoClient
from configs.config import Config
import logging as logger
def mongo_connection():
    mongo_url = Config.MONGODB_URI
    oracle_mongo_client = MongoClient(mongo_url)
    #oracle_database_name = mongo_url.split('/')[3]
    return oracle_mongo_client.get_database().name
    #[oracle_database_name]
