from pymongo import MongoClient
import os

class DBClient:

    __connection = None

    @classmethod
    def connnect(cls):
        if not cls.__connection:
            client = MongoClient(
                host=os.getenv('MONGO_HOST'),
                username=os.getenv('MONGO_USER'),
                password=os.getenv('MONGO_PASS'),
                authSource='admin'
            )
            db = client[os.getenv('MONGO_DB')]
            cls.__connection = db
        return cls.__connection