import unittest
from unittest.mock import patch
from assistant import Assistant
import json


class TestAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = Assistant()
    
    def test_suggest_word(self):
        with patch('assistant.requests.post') as mocked_post:
            mocked_post.return_value = 200
            mocked_post.json.return_value = {'choices': [{'message': {'content': {
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
                                                                        }
                                                                    }
                                                                ]
                                                            }
            expected_result = {
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
            self.assertEqual(self.assistant.suggest_word('context'), expected_result)
    def test_suggest_example(self):
        pass

    def test_suggest_word_of_the_day(self):
        pass

if __name__ == "__main__":
    unittest.main()