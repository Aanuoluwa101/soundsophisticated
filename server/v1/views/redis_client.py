import os
from dotenv import load_dotenv
import redis

load_dotenv()
redis_url = os.getenv('REDIS_URL_LOCAL')
redis_pool = redis.ConnectionPool.from_url(redis_url)
redis_client = redis.Redis(connection_pool=redis_pool)
