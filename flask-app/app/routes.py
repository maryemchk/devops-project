from flask import Blueprint, render_template
from .services import get_home_content

main = Blueprint('main', __name__)

@main.route('/')
def home():
    message, features = get_home_content()
    return render_template("home.html", message=message, features=features)
