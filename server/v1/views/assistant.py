from views import app_views
from flask import jsonify
from .utils.db import words_in_contexts
import json
from bson import json_util
from datetime import datetime
from .utils.get_last_7 import get_last_7
from .utils.db import word_of_the_day as word_of_the_day_collection
from .utils.dictionary import Dictionary
from .utils.assistant import Assistant


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
                suggested_word["data"]["pronunciation"] = dictionary.get_pronunciation(suggested_word["data"]["word"])
                insert_result = words_in_contexts.insert_one(suggested_word["data"])
                inserted_id = str(insert_result.inserted_id)
                suggested_word["data"]["_id"] = inserted_id  
                return json.loads(json_util.dumps(suggested_word["data"])), 201
        else: 
            return "Oops! Something went wrong", 500
    else:
        suggested_words_count = words_in_contexts.count_documents({})
        return str(suggested_words_count), 200
    

@app_views.route('/assistant/word_of_the_day', methods=['GET'])
def suggest_word_of_the_day():
    #we'll implement caching, such that this function is run only once in a day
    #we'll do that for the dictionary too

    word_of_the_day = word_of_the_day_collection.find_one({"date": str(datetime.today().date())})
    if word_of_the_day_collection:
        return json.loads(json_util.dumps(word_of_the_day)), 200
    
    last_7 = get_last_7()
    word_of_the_day = assistant.suggest_word_of_the_day(last_7)
    if word_of_the_day:
        search_result = dictionary.search(word_of_the_day)
        if search_result.status_code == 200:
            word_of_the_day = json.loads(search_result.data)
            word_of_the_day_collection.insert_one(word_of_the_day)
            return json.loads(json_util.dumps(word_of_the_day)), 200
            #return word["word"], 200 
    return "Error getting word of the day!", 500

#     data = {
#   "meanings": [
#     {
#       "definition": "\"Hello!\" or an equivalent greeting.",
#       "example": "Hello! how're you today",
#       "part_of_speech": "noun"
#     },
#     {
#       "definition": "To greet with \"hello\".",
#       "example": "Hello! how're you today",
#       "part_of_speech": "verb"
#     },
#     {
#       "definition": "A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.",
#       "example": "Hello, everyone.",
#       "part_of_speech": "interjection"
#     },
#     {
#       "definition": "A greeting used when answering the telephone.",
#       "example": "Hello? How may I help you?",
#       "part_of_speech": "interjection"
#     },
#     {
#       "definition": "A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.",
#       "example": "Hello? Is anyone there?",
#       "part_of_speech": "interjection"
#     },
#     {
#       "definition": "Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.",
#       "example": "You just tried to start your car with your cell phone. Hello?",
#       "part_of_speech": "interjection"
#     },
#     {
#       "definition": "An expression of puzzlement or discovery.",
#       "example": "Hello! What’s going on here?",
#       "part_of_speech": "interjection"
#     }
#   ],
#   "phonetic": "/həˈləʊ/",
#   "pronunciation": "https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3",
#   "word": "hello"
# }
    
#     return jsonify(data), 200

if __name__ == "__main__":
    print(suggest_word("grandma's birthday"))