#!/usr/bin/env python3
"""2. Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class to handle internalization

        Attributes:
          LANGUAGES: list of accepted languages
    """
    LANGUAGES = ['en', 'fr']


def get_locale():
    """Selects a language for each request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app, default_locale='en', default_timezone='UTC',
              locale_selector=get_locale)


@app.route('/')
def hello_world():
    """Handles the / route."""
    return render_template('2-index.html')
