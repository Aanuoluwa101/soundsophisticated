# # # import replicate

# # # system_role = "You are a helpful assistant on an application that suggests new words that can help a user sound sophisticated in their speaking or writing. You will be provided a context in which to suggest the word. Contexts can be a profession, a situation, an event etc. You are to respond only with json as examplified below 'statusCode': 200, 'context': 'asking for an explanation', 'word': 'Lucid', 'meaning': 'clear; easy to understand', 'example': 'let your explanation be lucid', 'part_of_speech': 'adjective', 'context_sounds_hilarious': true"
# # # prompt = "correct a child's bad behaviour"
# # # input = {
# # #     "prompt": prompt,
# # #     "prompt_template": f"{system_role} {prompt}"
# # # }

# # # output = replicate.run(
# # #    "meta/meta-llama-3-70b-instruct",
# # #   input=input
# # # )

# # # print(''.join(output))


# import requests

# def test_chatgpt_api(api_key, prompt):
#     url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "gpt-3.5-turbo-0125",
#         "messages": [{"role": "system", "content": prompt}]
#     }
#     response = requests.post(url, json=data, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# # Replace 'YOUR_API_KEY' with your actual API key

# import os
# from dotenv import load_dotenv
# load_dotenv()
# # Sample prompt
# prompt = "define electrolysis"

# api_key = os.getenv('OPENAI_APIKEY') 
# response = test_chatgpt_api(api_key, prompt)
# # # # Test the API
# print("Response from ChatGPT:", response)


# # # from db import word_of_the_day
# # # from datetime import datetime

# # # current_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

# # #     # Find document with date matching current date
# # # document = word_of_the_day.find_one({"date": current_date})

# # # print(str(datetime.now().date()))

# # from dotenv import load_dotenv
# # import os
# # load_dotenv()

# # uri = os.getenv('DB_URI')
# # #uri = "mongodb+srv://soundsophisticated:soundsophisticated123@mercymercy.dyidanr.mongodb.net/?retryWrites=true&w=majority&appName=MercyMercy"
# # #uri = 'mongodb://soundsophisticated:soundsophisticated123@localhost:27017/soundsophisticated'


# # data = [
# #   {
# #     "word": "pronunciation",
# #     "phonetic": "/pɹəˌnaʊn.siˈeɪ.ʃən/",
# #     "phonetics": [
# #       {
# #         "text": "/pɹəˌnaʊn.siˈeɪ.ʃən/",
# #         "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/pronunciation-us.mp3",
# #         "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=589419",
# #         "license": {
# #           "name": "BY-SA 3.0",
# #           "url": "https://creativecommons.org/licenses/by-sa/3.0"
# #         }
# #       }
# #     ],
# #     "meanings": [
# #       {
# #         "partOfSpeech": "noun",
# #         "definitions": [
# #           {
# #             "definition": "The formal or informal way in which a word is made to sound when spoken.",
# #             "synonyms": [],
# #             "antonyms": [],
# #             "example": "What is the pronunciation of \"hiccough\"?"
# #           },
# #           {
# #             "definition": "The way in which the words of a language are made to sound when speaking.",
# #             "synonyms": [],
# #             "antonyms": [],
# #             "example": "His Italian pronunciation is terrible."
# #           },
# #           {
# #             "definition": "The act of pronouncing or uttering something.",
# #             "synonyms": [],
# #             "antonyms": []
# #           }
# #         ],
# #         "synonyms": [],
# #         "antonyms": []
# #       }
# #     ],
# #     "license": {
# #       "name": "CC BY-SA 3.0",
# #       "url": "https://creativecommons.org/licenses/by-sa/3.0"
# #     },
# #     "sourceUrls": [
# #       "https://en.wiktionary.org/wiki/pronunciation"
# #     ]
# #   }
# # ]

# # import requests
# # import json
# # from constants import SUGGEST_WORD_OF_THE_DAY_SYSTEM_ROLE, SUGGEST_EXAMPLE_SYSTEM_ROLE, SUGGEST_WORD_SYSTEM_ROLE, payload, headers

# # def suggest_example(word_and_definition):
# #         messages = [{"role": "system", "content": f"{SUGGEST_EXAMPLE_SYSTEM_ROLE}"}]
# #         messages.append({"role": "user", "content": f"{word_and_definition}"})
# #         payload["messages"] = messages

# #         try:
# #            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
# #            if response.status_code == 200:
# #               return json.loads(response.json()["choices"][0]['message']['content'])
# #         except Exception as e:
# #            #we'll log these erros later
# #            print(e)


# # def extract_definitions(data):
# #     all_definitions = []
# #     for meaning in data["meanings"]:
# #         for definition in meaning["definitions"]:
# #             lean_definition = {
# #                 "word": data["word"], 
# #                 "part_of_speech": meaning["partOfSpeech"],
# #                 "definition": definition["definition"],
# #                 "example": definition.get("example", None)
# #             }
# #             all_definitions.append(lean_definition)

# #     return all_definitions


# # definitions = [
# #     {
# #         'word': 'pronunciation',
# #         'part_of_speech': 'noun',
# #         'definition': 'The formal or informal way in which a word is made to sound when spoken.',
# #         'example': 'What is the pronunciation of "hiccough"?'
# #     },
# #     {
# #         'word': 'pronunciation',
# #         'part_of_speech': 'noun',
# #         'definition': 'The way in which the words of a language are made to sound when speaking.',
# #         'example': None
# #     },
# #     {
# #         'word': 'pronunciation',
# #         'part_of_speech': 'noun',
# #         'definition': 'The act of pronouncing or uttering something.',
# #         'example': None
# #     }
# # ]


# # def check_example(definition):
# #     example = definition.get("example", None)
# #     if not example:
# #         result = suggest_example({"word": definition["word"], "definition": definition["definition"]})
# #         if result:
# #             example = result["example"]
# #     definition["example"]  = example



# # def process_definitions(all_definitions):
# #     # for definition in all_definitions:
# #     #     check_example(definition)

# #     with concurrent.futures.ThreadPoolExecutor() as executor:
# #         executor.map(check_example, all_definitions)
        
# #     print(all_definitions)


# # import time
# # import concurrent.futures


# # if __name__ == "__main__":
# #     start = time.time()
# #     all_defs = extract_definitions(data[0])
# #     processed = process_definitions(all_defs)
# #     end = time.time()

# #     print(f"Took {end-start} seconds")
# #print(extract_definitions(data[0]))



# from datetime import datetime

# print(datetime.now())

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print(l)

f(3)