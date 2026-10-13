#!/usr/bin/env python3
"""Flask routes for the Flatiron Cars company site."""

from flask import Flask
from markupsafe import escape

# Create the Flask application instance; __name__ tells Flask where to find resources.
app = Flask(__name__)

# Car models currently in the Flatiron fleet. The /<model> route checks against this list.
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index() -> str:
    """Default route: introduce the company."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model(model: str) -> str:
    """Model route: report whether the requested model is in the fleet.

    The `model` URL segment is passed in as a string. Matching is
    case-sensitive, so '/beedle' is not the same as '/Beedle'.
    The value is escaped before being echoed back to prevent HTML injection.
    """
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {escape(model)} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
