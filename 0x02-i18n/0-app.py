#!/usr/bin/env python3
"""0. Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Handles the / route."""
    return render_template('0-index.html')
