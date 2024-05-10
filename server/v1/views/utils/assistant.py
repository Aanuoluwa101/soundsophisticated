import requests
from .constants import SUGGEST_WORD_OF_THE_DAY_SYSTEM_ROLE, SUGGEST_EXAMPLE_SYSTEM_ROLE, SUGGEST_WORD_SYSTEM_ROLE, payload, headers
from dotenv import load_dotenv
import os
import json


load_dotenv()

class Assistant:
    url = os.getenv('CHATGPT_URL')
    #api_key = os.getenv('OPENAI_API_KEY')

    def suggest_word(self, context):
        messages = [{"role": "system", "content": f"{SUGGEST_WORD_SYSTEM_ROLE}"}]
        messages.append({"role": "user", "content": f"{context}"})
        payload["messages"] = messages

        return {
            "code": 200,
            "data": {
            "context": "trying to impress my music student",
            "word": "virtuosic",
            "definition": "extremely skillful",
            "example": "Your performance displayed a virtuosic mastery of the instrument, showcasing exceptional skill and emotion.",
            "part_of_speech": "adjective",
            "has_other_meanings": True
         }
      }
        # try:
        #     response = requests.post(Assistant.url, headers=headers, json=payload)
        #     print(response)
        #     if response.status_code == 200:
        #         return json.loads(response.json()["choices"][0]['message']['content'])
        # except Exception as e:
        #     print("entered here")
        #     #we'll log these erros later
        #     print(e)


    def suggest_example(self, word_and_definition):
        messages = [{"role": "system", "content": f"{SUGGEST_EXAMPLE_SYSTEM_ROLE}"}]
        messages.append({"role": "user", "content": f"{word_and_definition}"})
        payload["messages"] = messages

        return {
                    'code': 200, 
                    'example': 'The horror movie was so gory that I had to look away.'
                }
        # try:
        #    response = requests.post(Assistant.url, headers=headers, json=payload)
        #    if response.status_code == 200:
        #       return json.loads(response.json()["choices"][0]['message']['content'])
        # except Exception as e:
        #    #we'll log these erros later
        #    print(e)

    def suggest_word_of_the_day(self, last_7: list) -> str:
        messages = [{"role": "system", "content": f"{SUGGEST_WORD_OF_THE_DAY_SYSTEM_ROLE}"}]
        messages.append({"role": "user", "content": f"{last_7}"})
        payload["messages"] = messages

        #return "eerie"
        try:
           response = requests.post(Assistant.url, headers=headers, json=payload)
           if response.status_code == 200:
              return response.json()["choices"][0]['message']['content']
        except Exception as e:
           #we'll log these erros later
           print(e)
        