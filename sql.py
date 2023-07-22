## Python script to create SQLite database for Flask blog app
##
## Created 2023023, Jimmy Lela
## Updated 2023023, Jimmy Lela

import sqlite3

## Connect to (and create if needed) database, save connection as variable
with sqlite3.connect("blog.db") as blog_db_connection:

    ## create cursor object, save to variable
    blog_db_cursor = blog_db_connection.cursor()

    ## create posts table
    blog_db_cursor.execute("""
        CREATE table posts (title TEXT, post TEXT)
    """)

    ## Insert default data into posts table
    blog_db_cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    blog_db_cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    blog_db_cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    blog_db_cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')

