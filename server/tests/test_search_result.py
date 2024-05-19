import unittest
import json
from search_result import SearchResult


class TestSearchResult(unittest.TestCase):
    def test_search_result(self):
        search_result = SearchResult(200, "OK")

        self.assertEqual(search_result.status_code, 200)
        self.assertEqual(search_result.data, "OK")
        self.assertEqual(str(search_result), json.dumps({"code": 200, "data": "OK"}))


if __name__ == "__main__":
    unittest.main()