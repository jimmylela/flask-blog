## Python script to create SQLite database for Flask blog app
##
## Created 2023023, Jimmy Lela
## Updated 2023023, Jimmy Lela

## import modules
from flak import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

## DATABASE = 'blog.db'

## define Flask app - __name__ ?? 20230722
app = Flask(__name__)

## pulls in app configuration by looking for UPPERCASE variables - DAFUQ? 20230722
app.config.from_object(__name__)

## define function for connecting to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

## run if not imported from another instance and enable debug mode
if __name == '__main__':
    app.run(debug=True)
