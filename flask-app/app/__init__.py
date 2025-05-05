from flask import Flask

app = Flask(__name__)

from app import routes  # Make sure routes.py uses the same `app`
