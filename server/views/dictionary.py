from soundsophisticated import app_views
from flask import jsonify
from soundsophisticated.dictionary import Dictionary

dictionary = Dictionary()

@app_views.route('dictionary/<word>', methods=['GET'])
def search_dictionary(word: str):
    #print("got here")
    result = dictionary.search(word)
    if result.status_code != 200:
        return result.data, result.status_code
    return jsonify(result.data), result.status_code
    


if __name__ == "__main__":
    print(search_dictionary("hello"))