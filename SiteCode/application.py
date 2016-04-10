"""

This application file describes the backend framework to be used by flask in serving database information from the
associated mysql database.

"""

from flask import *
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

application = flask.

