'''
Created on Sep 27, 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@author: nor67
'''
import datetime
import re #to validate password format

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager #to handle user sessions
from flask_login import UserMixin
from flask_login import login_user, current_user, logout_user, login_required
#from sqlalchemy.orm import scoped_session,sessionmaker
#from forms import RegistrationForm, LoginForm

# Construct an instance of Flask class for webapp
app = Flask(__name__)
#to create secret key: comand prompt > python > import secrets > secrets.token_hex(16)
app.config['SECRET_KEY'] = '944db6da1ed6e8f03124d2f3b63fc31f'
#create database for usernames and passwords
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
global count
count = 0

#function to get user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    '''to create database to store users and passwords'''
    #columns in the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self): #how the object is printed
        return f"User('{self.username}')"

    def pylint_pass(self):
        '''to handle missing function in pylint'''
        print(self + 'pass')

@app.route('/')   # URL '/' to be handled by main() route handler
@app.route('/home')
def home():
    '''returns home.html'''
    return render_template('home.html')

@app.route("/about") # URL '/about' to be handled by about() route handler
@login_required
def about():
    '''creates variable of date and time to display and returns about.html'''
    now = datetime.datetime.now()
    now = now.strftime("%m-%d-%Y  %H:%M")
    return render_template('about.html', date_time=now)

@app.route("/recipes") # URL '/recipes' to be handled by recipes() route handler
@login_required
def recipes():
    '''returns recipes.html'''
    return render_template('recipes.html')

@app.route("/registration", methods=['GET', 'POST']) # URL "/registration" to be handled
def registration():
    '''for user to register'''
    #redirects user to home page if already signed in.
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    error = None

    #validate the password is in the correct format.
    password_format = False
    #uncommon = False
    if request.method == 'POST':
        while not password_format:
            #modified regular expression from 8 to 12 characters from https://stackoverflow.com
            if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$'
                            , request.form.get('password')):
                password_format = True
            else:
                error = (' Password must contain 12 characters, 1 upper and lower case ' +
                         'letter, 1 number and 1 special character. Please try again.')
                return render_template('registration.html', error=error)


        file = open("CommonPasswords.txt", "r+")
        common_passwords = [file.readlines()]
        password = request.form.get('password')

        #         if line in password:
        #             error = (' Password is compromised. Please try again.')
        for word in common_passwords:
            if str(word) in password:
                error = (' Password is compromised. Please try again.')
                return render_template('registration.html', error=error)
       
        file.close()
        #validate that the password and re-entered password matches
        if request.form.get('password') != request.form.get('repassword'):
            error = ' Passwords do not match. Please try again.'
            return render_template('registration.html', error=error)

        #adding user to database with hashed password
        hashed_pw = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
        user = User(username=request.form.get('username'), password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        #flash message that registration was successful
        flash(f'Registration completed for {user}.', 'success')
        return redirect(url_for('login'))

    return render_template('registration.html', error=error)

# URL "/login" to be handled by login() route handler
@app.route("/login", methods=['GET', 'POST'])
def login():
    '''to login to website and see other pages'''
    #redirects user to home page if already signed in.
    count = 0
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        #query database to check that username exists and store in variable user
        user = User.query.filter_by(username=username).first()
        #used for testing only for a login and password to work without encryption
        #         if username == 'admin' and password == '123':
        #             login_user(user)
        #             flash('Administrator login successful.', 'success')
        #             return redirect(url_for('home'))

        # used to count failed log in attempts
        failed_log = []
        #log failed attempts with ip address, date and time
        ip_address = request.environ['REMOTE_ADDR']
        now = datetime.datetime.now()
        time_stamp = now.strftime("%m-%d-%Y  %H:%M")
        #checks user exists and that there password is verified in database

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('You are now logged in!!', 'success')
            return redirect(url_for('home'))
        else:
            count += 1
            flash('Login Unsuccessful. Check username and password.', 'danger')
            #log failed attempts with ip address, date and time
            ip_address = request.environ['REMOTE_ADDR']
            now = datetime.datetime.now()
            now = now.strftime("%m-%d-%Y  %H:%M")
            #updating list to log failed attempts
            failed_log += str(ip_address) + '   ' + str(time_stamp)
            return render_template('login.html', count=count, ip_address=ip_address, time_stamp=now)
    return render_template('login.html', count=0, ip_address='ip_address', time_stamp='time_stamp')

#     error = None
# 
#     if request.method == 'POST':
#         if request.form.get('username') != 'admin' and request.form.get('password') != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    '''for user to review account that is signed into and direct to update password'''
    return render_template('account.html')

@app.route("/reset_password", methods=['GET', 'POST'])
@login_required
def reset_password():
    '''for user to update password: must be signed in an provide current password'''
#     #redirects user to home page if already signed in.
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
    error = None

    #validate the password is in the correct format.
    password_format = False

    if request.method=="POST":
        password=request.form.get("password")
        new_password=request.form.get("new_password")
        repassword=request.form.get("repassword")
        user = current_user
        #checks password is verified in database before allowing to change password
        if bcrypt.check_password_hash(user.password, password):
            #validate new password is in correct format
            while not password_format:
                #modified regular expression from 8 to 12 characters from https://stackoverflow.com
                if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$'
                                , new_password):
                    password_format = True
                else:
                    error = (' Password must contain 12 characters, 1 upper and lower case ' +
                         'letter, 1 number and 1 special character. Please try again.')
                    return render_template('reset_password.html', error=error)

                #validate that the password and re-entered password matches
                if new_password != repassword:
                    error = ' Passwords do not match. Please try again.'
                    return render_template('reset_password.html', error=error)

            #adding user to database with hashed password
            hashed_pw = bcrypt.generate_password_hash(new_password).decode('utf-8')
            user.password = hashed_pw
            db.session.commit()            
            flash('Your password has been changed. You are now able to log in.','success')
            logout_user()
            return redirect(url_for('login'))
        else:
            flash('Unsuccessful. Check username and password.', 'danger') 
            return render_template('reset_password.html')
    return render_template('reset_password.html', error=error)



if __name__ == '__main__':
    app.run(debug=True)
    