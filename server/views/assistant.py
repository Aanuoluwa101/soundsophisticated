from soundsophisticated import app_views, logger, words_in_contexts, word_of_the_day as wotd_collection
# from soundsophisticated import word_of_the_day as wotd_collection
from soundsophisticated.dictionary import Dictionary
from soundsophisticated.assistant import Assistant
from soundsophisticated.utils.constants import ONE_DAY
from soundsophisticated.utils.cache import redis_client
from soundsophisticated.utils.generate_error import generate_error
import json
from bson import json_util
from flask import request
# from .utils.dictionary import Dictionary
# from .utils.assistant import Assistant
# from .utils.constants import ONE_DAY
# from .redis_client import redis_client


#logger = logging.getLogger()
#comment
dictionary = Dictionary()
assistant = Assistant()


@app_views.route('assistant/suggest', methods=['GET', 'POST'])
def word_in_context():
    if request.method == 'POST':
        data = request.get_json()
        word = data.get('word', None)
        context = data.get('context', None)

        response = assistant.word_in_context(word, context)
        if response.status_code == 200:
            word = json.loads(json.loads(response.text)['choices'][0]['message']['content'])
            if word["code"] == 400:
                print("got here")
                return "Invalid word or context", 400
            else:
                word["data"]["context"] = context if context else "any"
                words_in_contexts.insert_one(word["data"])  
                return json.loads(json_util.dumps(word["data"])), 201
        elif response.status_code == 400:
            return response.text, response.status_code
        else: 
            logger.error(generate_error(request, response.http_response()))
            return "Something went Wrong", 500
    else:
        suggested_words_count = words_in_contexts.count_documents({})
        return str(suggested_words_count), 200
    

@app_views.route('/assistant/word_of_the_day', methods=['GET'])
def suggest_word_of_the_day():
    cached_wotd = redis_client.get('wotd')

    if cached_wotd:
        return cached_wotd, 200
    
    response = assistant.word_of_the_day()
    if response.status_code == 200:
        wotd = json.loads(response.text)['choices'][0]['message']['content']
        search_result = dictionary.search(wotd)
        if search_result.status_code == 200:
            wotd = search_result.data
            redis_client.set('wotd', json.dumps(wotd), ex=ONE_DAY)
            wotd_collection.insert_one(wotd)
            return json.loads(json_util.dumps(wotd)), 200
        
    logger.error(generate_error(response.http_response(), request))    
    return "Error getting word of the day!", 500

if __name__ == "__main__":
    print(suggest_word("grandma's birthday"))