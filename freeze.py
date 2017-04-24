
"""
Basic script for freezing a Flask app.
"""

from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR app - app doesn't change, tvshow is for tvshows.py
from repsanddemographics import app

app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
