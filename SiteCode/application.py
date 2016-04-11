"""

This application file describes the backend framework to be used by flask in serving database information from the
associated mysql database.

"""

from flask import *
from models import *

application = Flask(__name__)
application.config["DEBUG"] = True


@application.route('/')
def home_page():
    return render_template('Home.html')


@application.route('/about/')
def about_page():
    return render_template('About.html')


@application.route('/login/')
def login_page():
    return render_template('login.html')


@application.route('/register/')
def registration_page():
    return render_template('Register.html')


if __name__ == '__main__':
    application.run()
