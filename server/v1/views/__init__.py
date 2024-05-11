from flask import Blueprint
from .utils.db import ping_db
from flask_caching import Cache


result = ping_db()
if not result: 
    print("Database unreachable. Shutting down server")
    exit(1)

cache = Cache()
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/')
from .assistant import *
from .dictionary import *