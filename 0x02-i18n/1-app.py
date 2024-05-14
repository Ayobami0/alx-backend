#!/usr/bin/env python3
"""1. Basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class to handle internalization

        Attributes:
          LANGUAGES: list of accepted languages
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app, default_locale='en', default_timezone='UTC')


@app.route('/')
def hello_world():
    """Handles the / route."""
    return render_template('1-index.html')
