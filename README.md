# Wordbox API Documentation

API documentation for Wordbox (currently soundsophisticated). 

## Base URL
The base URL for all API routes is `https://soundsohpisticated.onrender.com/api/v1`.

## Routes

### 1. Suggest a Word in Context
- **Route:** `assistant/suggest`
- **Method:** POST
- **Description:** Suggests a word in context or an example sentence based on the provided word and context parameters.
- **Request Body:**
 - **Request Body:**
 ```json
 {
    "word": null,
    "context": "engineering",
}
```

- **Note on Request Body:** Word or context can be null but both cannot be null at thesame time
- Responses: 
    - **Success** 201 (CREATED)
```json
{
    "word": "example",
    "part_of_speech": "noun",
    "definition": "a thing characteristic of its kind or illustrating a general rule.",
    "example": "this is an example usage of the word.",
    "context": "usage"
}
```
- **Invalid Word or Context** - context or word doesn't make sense or is a number (400 Bad Request): `"Invalid word or context"`
- **Null word and context** (400 Bad Request): `"Word and context cannot be both null"`
- **Server Error** (500 Internal Server Error): `"Something went wrong"`

### 2. Get number of suggested words and examples 

- **Route:** `assistant/suggest`
- **Method:** GET
- **Description:** Returns the total number of words and sentence examples suggested by the application
- **Response code:** 200 OK
- **Response Body:** 55


### 3. Get word of the day

- **Route:** `assistant/word_of_the_day`
- **Method:** GET
- **Description:** Returns the word of the day. If the word of the day is cached, it will return the cached word. Otherwise, it fetches a new word of the day and caches it.
- **Response Code:** 200 OK
- **Response Body:**
```json
  {
  "word": "serendipity",
  "phonetic": "/ˌsɛ.ɹən.ˈdɪ.pɪ.ti/",
  "meanings": [
    {
      "word": "serendipity",
      "part_of_speech": "noun",
      "definition": "A combination of events which have come together by chance to make a surprisingly good or wonderful outcome.",
      "example": "It was pure serendipity that I found my long-lost childhood friend at the airport."
    },
    {
      "word": "serendipity",
      "part_of_speech": "noun",
      "definition": "An unsought, unintended, and/or unexpected, but fortunate, discovery and/or learning experience that happens by accident.",
      "example": "The scientist made a serendipity discovery while conducting unrelated experiments in the lab."
    }
  ]
}
```
- **Server Error** (500 Internal Server Error): `"Error getting word of the day"`

### 4. Search Dictionary
- **Route:** `/dictionary/<word>`
- **Method:** GET
- **Request Parameters:** word (required) - The word to be searched.
- **Description:** Searches for the given word in the dictionary and returns its definition, pronunciation, and example usage.
- **Response**: 
    - Success (200 OK):
```json
    {
    "word": "example",
    "phonetic": "ɪɡˈzɑːmp(ə)l",
    "meanings": [
        {
            "part_of_speech": "noun",
            "definitions": [
                {
                    "definition": "a thing characteristic of its kind or illustrating a general rule.",
                    "example": "this is an example usage of the word."
                }
            ]
        }
    ]
}
```
- **Not Found** (404 Not Found): `"Sorry pal, we couldn't find definitions for the word you were looking for."`
- **Server Error** (500 Internal Server Error): `"Server Error"`

