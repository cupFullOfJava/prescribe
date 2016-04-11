"""

This application file describes the backend framework to be used by flask in serving database information from the
associated mysql database.

"""

from flask import *
from models import *

application = Flask(__name__)
application.config["DEBUG"] = True


# Render the Home.html template at the base url ("/")
@application.route('/')
def home_page():
    return render_template('Home.html')


# Render the about page template at the '/about/' url
@application.route('/about/')
def about_page():
    return render_template('About.html')


# Render the login page template at the '/login/' url
@application.route('/login/')
def login_page():
    return render_template('login.html')


# Render the registration page template at the '/register/' url
@application.route('/register/')
def registration_page():
    return render_template('Register.html')

# Runs the application
if __name__ == '__main__':
    application.run()
