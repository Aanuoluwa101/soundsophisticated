from .db import word_of_the_day
#from db import word_of_the_day
from datetime import datetime, timedelta


seven_days_ago = datetime.now() - timedelta(days=7)

def get_last_7():
    try:
        result = word_of_the_day.aggregate([
            {
                "$match": {
                    "date": {
                        "$gte": seven_days_ago
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "word": 1
                }
            }
        ])
        if not result:
            return []
        return [word['word'] for word in list(result)]
    except Exception as e:
        print(e)
        return []
    
if __name__ == "__main__":
    print(get_last_7())