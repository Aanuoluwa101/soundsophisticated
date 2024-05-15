from flask import Blueprint
from .utils.db import ping_db
from .redis_client import ping_redis


result = ping_db()
if not result: 
    print("Database unreachable. Shutting down server")
    exit(1)

result = ping_redis()
if not result: 
    print("Cache unreachable. Shutting down server")
    exit(1)


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/')
from .assistant import *
from .dictionary import *