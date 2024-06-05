data = [
    {'definition': 'some definition',},
    {'definition': 'another definition',}
]

#Say you wanted to process this data. 
#Call a function get_example
# on every definition in the list. 
#get_example makes an http request to get an example for each defintion

#get_example
import requests 
base_url = 'https://examples.com/examples'
def get_example(definition):
    try:
        response = requests.get(f"{base_url}/{definition}")
        if response.status_code == 200:
            example = response.json()["choices"][0]['message']['content']
    except Exception as e:
        example = None
        print(e)
    finally:
        definition["example"] = example
        

#use a for loop: 6.2 seconds
def process_data(data):
    for definition in data:
        get_example(definition)

#create a thread to process each item (multithreading): 4.3 seconds
import concurrent.futures
def process_data(data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
         executor.map(get_example, data)

#Python's GIL (Global Interpreter Lock) does not have much impact on 
#the performance of I/O-bound multi-threaded programs, making some
#parallelism achievable in such programs .
#http requests are I/O-bound, thus the shorter processing time.