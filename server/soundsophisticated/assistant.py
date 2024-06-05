import requests
from dotenv import load_dotenv
import os
import json
from .utils.get_last_7 import get_last_7
from .utils.constants import (
    WORD_PROPMT_SYSTEM_ROLE,
    WORD_OF_THE_DAY_PROMPT_SYSTEM_ROLE,
    EXAMPLE_BY_DEFINITION_PROMPT_SYSTEM_ROLE,
    EXAMPLE_BY_CONTEXT_PROMPT_SYSTEM_ROLE,
    EXAMPLE_BY_ANY_CONTEXT_PROMPT_SYSTEM_ROLE,
    headers,
    payload   
)

#from utils.get_last_7 import get_last_7
#from utils.constants import SUGGEST_WORD_OF_THE_DAY_SYSTEM_ROLE, SUGGEST_EXAMPLE_SYSTEM_ROLE, SUGGEST_WORD_SYSTEM_ROLE, payload, headers



load_dotenv()

class Assistant:
    def __init__(self) :
        self.url = os.getenv('CHATGPT_URL')

    class AssistantResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def http_response(self):
            return {'text': self.text, 'status_code': self.status_code}
        
        def __str__(self):
            return f"{self.text}, {self.status_code}"
        

    # def suggest_word(self, context):
    #     messages = [{"role": "system", "content": f"{SUGGEST_WORD_SYSTEM_ROLE}"}]
    #     messages.append({"role": "user", "content": f"{context}"})
    #     payload["messages"] = messages

    #   #   return {
    #   #       "code": 200,
    #   #       "data": {
    #   #       "context": "trying to impress my music student",
    #   #       "word": "virtuosic",
    #   #       "definition": "extremely skillful",
    #   #       "example": "Your performance displayed a virtuosic mastery of the instrument, showcasing exceptional skill and emotion.",
    #   #       "part_of_speech": "adjective",
    #   #       "has_other_meanings": True
    #   #    }
    #   # }
    #     try:
    #         if int(context):
    #             return "Invalid context: integer", 400
    #     except ValueError:
    #         pass
        
    #     try:
    #         response = requests.post(Assistant.url, headers=headers, json=payload)
    #         #print(response)
    #         if response.status_code == 200:
    #             return json.loads(response.json()["choices"][0]['message']['content'])
    #     except Exception as e:
    #         print("entered here")
    #         #we'll log these erros later
    #         print(e)

    def call_chatgpt(self, system_role, prompt):
        #print(prompt)
        messages = [{"role": "system", "content": system_role},
                    {"role": "user", "content": prompt}]
        payload["messages"] = messages

        try:
           response = requests.post(self.url, headers=headers, json=payload)
           return self.AssistantResponse(response.text, response.status_code)
        except Exception as e:
           return self.AssistantResponse("Internal Server Error", 500)


    def word_in_context(self, word, context):
        if context:
            try:
                int(context)
                return self.AssistantResponse("Invalid context: integer", 400)
            except ValueError:
                pass

            if word:
                system_role = EXAMPLE_BY_CONTEXT_PROMPT_SYSTEM_ROLE
                prompt = f"{{'word': '{str(word)}', 'context': '{str(context)}'}}"
            else:
                system_role = WORD_PROPMT_SYSTEM_ROLE
                prompt = context
        elif word and not context:
            system_role = EXAMPLE_BY_ANY_CONTEXT_PROMPT_SYSTEM_ROLE
            prompt = word 
        else:
            return self.AssistantResponse("Word and context cannot be both null", 400)

        return self.call_chatgpt(system_role, prompt)  

    def example_by_definition(self, word_and_definition):
        system_role = EXAMPLE_BY_DEFINITION_PROMPT_SYSTEM_ROLE
        word = word_and_definition['word']
        definition = word_and_definition['definition']
        prompt = f"{{'word': '{str(word)}', 'context': '{str(definition)}'}}"

        return self.call_chatgpt(system_role, prompt)
     # return {
        #             'code': 200, 
        #             'example': 'The horror movie was so gory that I had to look away.'
        #         }

    def word_of_the_day(self) -> str:
        #last_7 = get_last_7()
        last_7 = ['eerie', 'resplendent', 'audacious', 'gory', 'sultry']
        system_role = WORD_OF_THE_DAY_PROMPT_SYSTEM_ROLE
        prompt = f"suggest a word for the day. Avoid the following words: {last_7}. Your response should be the word only"
        

        return self.call_chatgpt(system_role, prompt)
        # return "eerie"
        # try:
        #    #print("entered here")
        #    response = requests.post(Assistant.url, headers=headers, json=payload)
        #    if response.status_code == 200:
        #       return response.json()["choices"][0]['message']['content']
        # except Exception as e:
        #    #we'll log these erros later
        #    print(e)

          

if __name__ == "__main__":
    assistant = Assistant()
    #print(assistant.word_in_context("gory")) #any context
    #print(assistant.word_in_context(context="sfgeg345h")) #context only
    #print(assistant.word_in_context("gory", "technician")) #a context that makes sense
    #print(assistant.word_in_context("gory", "class"))   #a context that doesn't make sense, ended up being valid
    #print(assistant.word_in_context("gory", "sdfffsoief")) #gibberish context...we have to revisit this
    #print(assistant.word_in_context("gory", "232")) #number context
    #print(assistant.word_in_context()) #no context no word

    # print(assistant.call_chatgpt("hello", "sfgeg345h"))

    #example by definition
    #word_and_def = {'word': 'felicity', 'definition': "An apt and pleasing style in speech, writing, etc."}
    #print(assistant.example_by_definition(word_and_def))

    #word of the day
    print(assistant.word_of_the_day())