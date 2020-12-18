from . import bp as intro
from flask import render_template


@intro.route('/')
def index():
    return render_template('index.html')