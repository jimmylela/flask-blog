## Flask blog app from RealPython 2
##
## Created 20230723, Jimmy Lela
## Updated 20230703, Jimmy Lela

## import Flask and other classes from flask module
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

## import sqlite3 module and wraps function from functools, which extends the capabilities of functions
import sqlite3
from functools import wraps

## define configuration variables
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

## instantiate a Flask class object, pass it the __name_variable, which 
## will have the value of this Python file (blog.py), telling Flask
## to look for other resources in the same directory using all caps variables
## Note: must precede function definitions that use it 
## Why doesn't it have the value of "__main__" if it's ran directly? - 20230729
## Why is this needed if the variables are defined in this same file? - 20230730
app = Flask(__name__)

## pull in app configuration by looking for UPPERCASE variables
## Why does __name__ have to be passed again if it already was above? - 20230730
app.config.from_object(__name__)

## databse function
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

## login function
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again.'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error), status_code

## logout function
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

## require login function
## Where does the value for test come from? The request somehow I assume. - 20230730
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap


## main page function
@app.route('/main')
@login_required
def main():
    return render_template('main.html')

## run if not imported from another instance and enable debug mode
if __name__ == '__main__':
    app.run(debug=True)
