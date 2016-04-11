"""

This application file describes the backend framework to be used by flask in serving database information from the
associated mysql database.

"""

from flask import request, render_template, Flask
import peewee
from MySQLdb import MySQLError
from werkzeug.security import generate_password_hash, check_password_hash
from models import *

application = Flask(__name__)
application.config["DEBUG"] = True


# Connect to the database whenever a request needs to be made
@application.before_request
def connect_db():
    database.connect()


# Disconnect from the database after requests in order to prevent database connection timeouts
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
    return render_template('Register.html', flags={}, values={})


# URL endpoint for registration
@application.route('/submit-registration/', methods=['POST'])
def submit_reg():
    # Instantiate repeatemail and repeatpwd flags in flags dictionary to false
    flags = {
        "repeatemail": False,
        "repeatpwd": False
    }

    # Instantiate a values dictionary
    values ={}
    # Define a list of form input fields
    fields = ['fname', 'lname', 'email', 'pwd1', 'pwd2']
    # Iterate through fields, and set the values in the values dictionary accordingly.
    # if the length of the field is zero, set a flag for it in the flags dictionary
    for field in fields:
        value = request.form[field]
        if len(value) == 0:
            flags[field] = True
        else:
            flags[field] = False
        values[field] = value
    if all(not(flags[field]) for field in fields):
        print('All Flags good')
        # Check if the user entered the same password in both password fields
        if values['pwd1'] == values['pwd2']:
            # If passwords check out, try to add a user to the database
            try:
                Users.create(firstname=values['fname'],
                             lastname=values['lname'],
                             email=values['email'],
                             user_pw=generate_password_hash(values['pwd1']))
                print 'User Added'
            except MySQLError as er:
                print er.message
            # If the email address given already exists in the database, set the repeatemail flag to True
            # and render the template again
            except IntegrityError:
                flags['repeatemail'] = True
                render_template('Register.html', flags=flags, values=values)
        # If the passwords do not match, set the repeatpwd flag to true, and render the template again
        else:
            flags["repeatpwd"] = True
            render_template('Register.html', flags=flags, values=values)
    # If some of the fields have empty strings for values, render the template again
    else:
        return render_template('Register.html', flags=flags, values=values)
    return render_template('Register.html', flags=flags, values=values)


# This url corresponds with the endpoint for user login requests.
@application.route('/user-login/', methods=['POST'])
def login():
    email = request.form['email']
    passwd = request.form['pwd']
    no_user = False
    # Tries to find the user in the database by email
    try:
        user = Users.get(Users.email == email)
        if check_password_hash(user.user_pw, passwd):
            print 'User '+user.firstname+' has successfully logged on.'
            no_user = False
        else:
            # If the password doesn't match the one found in the database, Set the no_user flag to True
            no_user = True
    except MySQLError as er:
        print er.message
    # If a user with the given email address doesn't exist in the database, set the no_user flag to True
    except peewee.DoesNotExist as er:
        no_user = True

    # no_user flag is passed into the html as a variable to trigger a form error graphic.
    return render_template('login.html', no_user=no_user)

# Runs the application
if __name__ == '__main__':
    application.run()
