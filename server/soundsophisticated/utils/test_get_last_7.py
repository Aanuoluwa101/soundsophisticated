import unittest
from unittest.mock import patch, MagicMock

import pymongo.errors
from get_last_7 import get_last_7
import pymongo


class TestGetLast7(unittest.TestCase):
    @patch('get_last_7.word_of_the_day')
    def test_get_last_7(self, mock_word_of_the_day):
        mock_word_of_the_day.aggregate.return_value = [{"_id": "1", "word": "one"},
                                                        {"_id": "2", "word": "two"},
                                                        {"_id": "3", "word": "three"}]
        self.assertGreater(len(get_last_7()), 0)

    @patch('get_last_7.word_of_the_day')
    def test_get_last_7_empty(self, mock_word_of_the_day):
        mock_word_of_the_day.aggregate.return_value = pymongo.errors.ConnectionFailure()

        self.assertEqual(len(get_last_7()), 0)


if __name__ == "__main__":
    unittest.main()