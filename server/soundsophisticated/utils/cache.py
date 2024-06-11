import os
from dotenv import load_dotenv
import redis

load_dotenv()
redis_url = os.getenv('REDIS_URL')
print(f"redis url is {redis_url}")
redis_client = redis.from_url(redis_url)


def ping_cache():
    try:
        redis_client.ping()
        print("Cache ready! Good to go!")
        return True
    except redis.ConnectionError as e:
        return False


if __name__ == "__main__":
    ping_cache()