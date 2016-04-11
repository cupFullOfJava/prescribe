"""

This application file describes the backend framework to be used by flask in serving database information from the
associated mysql database.

"""

from flask import request, render_template, Flask
from peewee import PeeweeException
from werkzeug.security import generate_password_hash, check_password_hash
from models import *

application = Flask(__name__)
application.config["DEBUG"] = True


@application.before_request
def connect_db():
    database.connect()


@application.teardown_request
def drop_db(exc):
    if not database.is_closed():
        database.close()


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


# URL endpoint for registration
@application.route('/submit-registration/', methods=['POST'])
def submit_reg():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    pwd1 = request.form['pwd1']
    pwd2 = request.form['pwd2']
    if pwd1 == pwd2:
        try:
            Users.create(firstname=fname,
                         lastname=lname,
                        email=email,
                        user_pw=generate_password_hash(pwd1))
            print 'User Added'
        except PeeweeException as er:
            print er.message

    return render_template('Register.html')


# Runs the application
if __name__ == '__main__':
    application.run()
