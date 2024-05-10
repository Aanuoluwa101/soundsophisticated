const data = [
  {
    "word": "pronunciation",
    "phonetic": "/pɹəˌnaʊn.siˈeɪ.ʃən/",
    "phonetics": [
      {
        "text": "/pɹəˌnaʊn.siˈeɪ.ʃən/",
        "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/pronunciation-us.mp3",
        "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=589419",
        "license": {
          "name": "BY-SA 3.0",
          "url": "https://creativecommons.org/licenses/by-sa/3.0"
        }
      }
    ],
    "meanings": [
      {
        "partOfSpeech": "noun",
        "definitions": [
          {
            "definition": "The formal or informal way in which a word is made to sound when spoken.",
            "synonyms": [],
            "antonyms": [],
            "example": "What is the pronunciation of \"hiccough\"?"
          },
          {
            "definition": "The way in which the words of a language are made to sound when speaking.",
            "synonyms": [],
            "antonyms": [],
            "example": "His Italian pronunciation is terrible."
          },
          {
            "definition": "The act of pronouncing or uttering something.",
            "synonyms": [],
            "antonyms": []
          }
        ],
        "synonyms": [],
        "antonyms": []
      }
    ],
    "license": {
      "name": "CC BY-SA 3.0",
      "url": "https://creativecommons.org/licenses/by-sa/3.0"
    },
    "sourceUrls": [
      "https://en.wiktionary.org/wiki/pronunciation"
    ]
  }
]



const suggestion = {
  "context": "trying to impress my music student",
  "definition": "extremely skillful",
  "example": "Your performance displayed a virtuosic mastery of the instrument, showcasing exceptional skill and emotion.",
  "has_other_meanings": true,
  "part_of_speech": "adjective",
  "pronunciation": "unavailable",
  "word": "virtuosic"
}

const processedData = {
  "meanings": [
    {
      "definition": "\"Hello!\" or an equivalent greeting.",
      "example": "Hello! how're you today",
      "part_of_speech": "noun"
    },
    {
      "definition": "To greet with \"hello\".",
      "example": "Hello! how're you today",
      "part_of_speech": "verb"
    },
    {
      "definition": "A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.",
      "example": "Hello, everyone.",
      "part_of_speech": "interjection"
    },
    {
      "definition": "A greeting used when answering the telephone.",
      "example": "Hello? How may I help you?",
      "part_of_speech": "interjection"
    },
    {
      "definition": "A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.",
      "example": "Hello? Is anyone there?",
      "part_of_speech": "interjection"
    },
    {
      "definition": "Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.",
      "example": "You just tried to start your car with your cell phone. Hello?",
      "part_of_speech": "interjection"
    },
    {
      "definition": "An expression of puzzlement or discovery.",
      "example": "Hello! What’s going on here?",
      "part_of_speech": "interjection"
    }
  ],
  "phonetic": "/həˈləʊ/",
  "pronunciation": "https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3",
  "word": "hello"
}
export default suggestion;