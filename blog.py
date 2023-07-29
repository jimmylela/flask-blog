## Python script to create SQLite database for Flask blog app
##
## Created 20230723, Jimmy Lela
## Updated 20230729, Jimmy Lela

## import Flask and other classes from flask module
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

## import sqlite3 module
import sqlite3

## define configuration variables
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'


## instantiate a Flask class object, pass it the __name_variable, which 
## will have the value of this Python file (blog.py), telling Flask
## to look for other resources in the same directory using all caps variables
## Why doesn't it have the value of "__main__" if it's ran directly? - 20230729
app = Flask(__name__)

## pull in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

## define function for connecting to database
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

    return render_template('login.html')

## main page function
@app.route('/main')
def main():
    return render_template('main.html')

## run if not imported from another instance and enable debug mode
if __name__ == '__main__':
    app.run(debug=True)
