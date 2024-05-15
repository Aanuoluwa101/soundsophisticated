from soundsophisticated import app_views
from soundsophisticated import words_in_contexts, word_of_the_day as wotd_collection
# from soundsophisticated import word_of_the_day as wotd_collection
from soundsophisticated.dictionary import Dictionary
from soundsophisticated.assistant import Assistant
from soundsophisticated.utils.constants import ONE_DAY
from soundsophisticated.utils.cache import redis_client
import json
from bson import json_util
# from .utils.dictionary import Dictionary
# from .utils.assistant import Assistant
# from .utils.constants import ONE_DAY
# from .redis_client import redis_client


dictionary = Dictionary()
assistant = Assistant()


@app_views.route('assistant/suggest')
@app_views.route('assistant/suggest/<context>', methods=['POST'])
def suggest_word(context=None):
    if context:
        try:
            if int(context):
                return "Invalid context: integer", 400
        except ValueError:
            pass
            
        suggested_word = assistant.suggest_word(context)
        if suggested_word:
            if suggested_word["code"] == 400:
                return "Invalid context: doesn't make sense", 400
            else:
                words_in_contexts.insert_one(suggested_word["data"])
                # inserted_id = str(insert_result.inserted_id)
                # suggested_word["data"]["_id"] = inserted_id  
                return json.loads(json_util.dumps(suggested_word["data"])), 201
        else: 
            return "Oops! Something went wrong", 500
    else:
        suggested_words_count = words_in_contexts.count_documents({})
        return str(suggested_words_count), 200
    

@app_views.route('/assistant/word_of_the_day', methods=['GET'])
def suggest_word_of_the_day():
    cached_wotd = redis_client.get('wotd')

    if cached_wotd:
        return cached_wotd, 200
    
    wotd = assistant.suggest_word_of_the_day()
    if wotd:
        search_result = dictionary.search(wotd)
        if search_result.status_code == 200:
            wotd = search_result.data
            redis_client.set('wotd', json.dumps(wotd), ex=ONE_DAY)
            wotd_collection.insert_one(wotd)
            return json.loads(json_util.dumps(wotd)), 200
    return "Error getting word of the day!", 500

if __name__ == "__main__":
    print(suggest_word("grandma's birthday"))