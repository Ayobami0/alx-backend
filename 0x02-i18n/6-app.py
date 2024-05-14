#!/usr/bin/env python3
"""3. Parametrize templates"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Gets a user by their id specified in the query"""
    id = request.args.get('login_as')
    if not id:
        return None
    user = users.get(int(id), None)
    if not user:
        return None
    return user


class Config:
    """Config class to handle internalization

        Attributes:
          LANGUAGES: list of accepted languages
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app, default_locale='en', default_timezone='UTC')


@babel.localeselector
def get_locale():
    """Select a language for each request"""
    query = request.args.get('locale', None)

    if query:
        return query

    user = g.get('user', None)
    if user is not None:
        return user.locale
    lang = request.headers.get('Accept-Language')

    if lang:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Runs before each request"""
    cur_user = get_user()
    g.user = cur_user


@app.route('/')
def hello_world():
    """Handles the / route."""
    return render_template('6-index.html', user=g.user)
