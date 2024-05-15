import requests
import json
from dotenv import load_dotenv
import os
import concurrent.futures
import time
from .search_result import SearchResult
from .assistant import Assistant



load_dotenv()
assistant = Assistant()

class Dictionary:
    url = os.getenv('DICTIONARYAPI_URL')

    def search(self, word):
        try:
            response = requests.get(f"{Dictionary.url}/{word}")
            if response.status_code == 200:
                self.data = json.loads(response.text)[0]

                result = self.process_search_result()
                # return json.dumps(data), 200
                return SearchResult(200, result)
                #return data
            elif response.status_code == 404:
                return SearchResult(404, json.loads(response.text)["message"])
            else: 
                return SearchResult(500, "Server Error")
        except Exception as e:
            print("here")
            #raise e
            return SearchResult(500, "Server Error")

    def extract_pronunciation(self):
        phonetics = self.data["phonetics"]
        for phonetic in phonetics:
            audio = phonetic.get("audio", None)
            if audio:
                return audio
            
    def extract_phonetic(self):
        phonetic = self.data.get("phonetic", None)
        if not phonetic:
            for item in self.data["phonetics"]:
                phonetic = item.get('text', None)
                if phonetic:
                    return phonetic
        return phonetic
            
        
    def check_example(self, definition):
        example = definition.get("example", None)
        if not example:
            result = assistant.suggest_example({"word": definition["word"], "definition": definition["definition"]})
            if result:
                example = result["example"]
        definition["example"]  = example

    def extract_definitions(self):
        all_definitions = []
        for meaning in self.data["meanings"]:
            for definition in meaning["definitions"]:
                lean_definition = {
                    "word": self.data["word"], 
                    "part_of_speech": meaning["partOfSpeech"],
                    "definition": definition["definition"],
                    "example": definition.get("example", None)
                }
                all_definitions.append(lean_definition)

        return all_definitions
    
    def process_definitions(self):
        all_definitions = self.extract_definitions()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.check_example, all_definitions)
        return all_definitions
        
    def process_search_result(self):
        return {
            "word": self.data["word"],
            "phonetic": self.extract_phonetic(),
            "meanings": self.process_definitions()
        }
    
    def get_pronunciation(self, word):
        try:
            response = requests.get(Dictionary.url + word)
            if response.status_code == 200:
                phonetics = response.json()[0]["phonetics"]
                for phonetic in phonetics:
                    audio = phonetic.get("audio", None)
                    if audio:
                        return audio
        except Exception as e: 
            #we'll log these errors in a file later
            pass


if __name__ == "__main__":
    start = time.time()

    dic = Dictionary()
    print(dic.search("hello"))

    end = time.time()
    print(f"Took {end-start} seconds")
