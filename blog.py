## Python script to create SQLite database for Flask blog app
##
## Created 20230723, Jimmy Lela
## Updated 20230729, Jimmy Lela

## import Flask and other classes from flask module
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

## import sqlite3 module
import sqlite3

## save database name to variable
DATABASE = 'blog.db'

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

## run if not imported from another instance and enable debug mode
if __name == '__main__':
    app.run(debug=True)
