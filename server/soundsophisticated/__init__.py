from flask import Blueprint
from .utils.db import ping_db, word_of_the_day, words_in_contexts
from .utils.cache import ping_cache



result = ping_db()
if not result: 
    print("Database unreachable. Shutting down server")
    exit(1)

result = ping_cache()
if not result: 
    print("Cache unreachable. Shutting down server")
    exit(1)


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/')
from views.assistant import *
from views.dictionary import *