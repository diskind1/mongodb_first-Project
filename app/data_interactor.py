from anyio import ConnectionFailed
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
import os
from dotenv import load_dotenv
load_dotenv()


class DB_Connection:

    client = None
    
    @staticmethod
    def connect_to_db():
        try:
            DB_Connection.client = MongoClient(
                host=os.getenv("MONGO_HOST"),
                port=int(os.getenv("MONGO_PORT")),
                appname=(os.getenv("MONGO_NAME"))
                # username=os.getenv("DB_USER"),
                # password=os.getenv("DB_PASSWORD"),
                # authSource=os.getenv("AUTH_SOURCE")
            )

            DB_Connection.client.admin.command("ping")
            print("✓ Successfully connected to MongoDB!")

            return DB_Connection.client

        except ConnectionFailed as e:
            print(f"✗ Failed to connect to MongoDB: {e}")
            print("Make sure MongoDB is running on localhost:27017")
            return None
        
    @staticmethod
    def get_client():
        if DB_Connection.client is None:
            DB_Connection.connect_to_db()
        return DB_Connection.client
    
    @staticmethod
    def get_database() -> Database:
        client = DB_Connection.get_client()
        return client['contacts_db']
    
    @staticmethod
    def get_contects_coll() -> Collection:
        db = DB_Connection.get_database()
        return db['contacts']

