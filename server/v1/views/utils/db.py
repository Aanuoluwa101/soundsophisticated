
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from pymongo.server_api import ServerApi


load_dotenv()
uri = os.getenv('DB_URI')

client = MongoClient(uri)
db = client.soundsophisticated
words_in_contexts = db.wordsincontexts
word_of_the_day = db.wordoftheday


def ping_db():
    try:
        client.admin.command('ping')
        print("Database ready! Good to go")
        return True
    except Exception as e:
        print(e)


# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

if __name__ == "__main__":
    ping_db()