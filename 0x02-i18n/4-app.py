#!/usr/bin/env python3
"""
Force locale with URL parameter
"""


from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)


class Config:
    '''configures available languages'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use the Config class as configuration for the Flask app
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''match best locale with our supported languages'''
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(
        app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''Hello world'''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
