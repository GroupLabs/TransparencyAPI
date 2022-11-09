from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

def connectMongo():
    # Connection
    conn_str = f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}@cluster0.dm2jouu.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(conn_str)

    return client