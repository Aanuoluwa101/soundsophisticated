from flask import Flask
from views import app_views
from dotenv import load_dotenv
from flask_cors import CORS
import os
from flask_caching import Cache
from views import cache



load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = os.getenv('REDIS_URL')

cache.init_app(app)
app.register_blueprint(app_views)
 


if __name__ == '__main__':
    app.run(debug=True)