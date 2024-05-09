import json 

class SearchResult:
    def __init__(self, status_code, data) -> None:
        self.status_code = status_code
        self.data = data


    def __str__(self) -> str:
        return json.dumps({"code": self.status_code, "data": self.data})