from soundsophisticated.assistant import Assistant
from soundsophisticated.dictionary import Dictionary
from .cache import redis_client
from .db import word_of_the_day as wotd_collection
from .constants import ONE_DAY
import logging
from datetime import datetime
import json


logging.basicConfig(filename='wotd_errors.log', level=logging.ERROR)
logger = logging.getLogger()



def  word_of_the_day():
    assistant = Assistant()
    dictionary = Dictionary()

    wotd = assistant.suggest_word_of_the_day()
    if not wotd:
        logger.error(f"Error Generating word of the day at {str(datetime.now())}")

    search_result = dictionary.search(wotd)
    if search_result.status_code == 200:
        wotd = search_result.data
        redis_client.set('wotd', json.dumps(wotd), ex=ONE_DAY)
        wotd_collection.insert_one(wotd)
        print(wotd)
    else: 
        logger.error(f"Error Generating word of the day at {str(datetime.now())}", str(search_result))
       

if __name__ == '__main__':
    word_of_the_day()