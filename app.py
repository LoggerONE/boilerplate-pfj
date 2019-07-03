import os
import redis #pip install redis

from flask import Flask

from os.path import join, dirname
from dotenv import load_dotenv #pip install -U python-dotenv
# Load .env
dotenv_path = join(dirname(__file__), '.env').encode('utf8').strip()
load_dotenv(dotenv_path)

app = Flask(__name__)


@app.route('/')
def hello():
    return os.environ.get("APP_NAME")

if __name__ == '__main__':
    app.run(port = os.environ.get("PORT") )