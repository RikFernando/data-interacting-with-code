# pylint: disable=missing-docstring, C0103
import sqlite3
conn = sqlite3.connect('data/movies.sqlite')
x = conn.cursor()

def directors_count(db):
    # return the number of directors contained in the database
    db.execute("SELECT COUNT(*) FROM directors")
    rows = db.fetchone()
    return rows[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("SELECT name FROM directors ORDER BY name ASC")
    rows = db.fetchall()
    director_names = [row[0] for row in rows]
    return director_names


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db.execute('''SELECT title FROM movies WHERE title LIKE "% love%"
               OR title LIKE "%love.%" OR title LIKE "%love,%"
               OR LIKE "%love'% OR LIKE"%love %""ORDER BY title ASC''')
    rows = db.fetchall()
    love_movie_names = [row[0] for row in rows]
    return love_movie_names

def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    db.execute(f'SELECT count(*) FROM directors WHERE name LIKE "%{name}%"')
    rows = db.fetchone()
    return rows[0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    db.execute(f'''SELECT title FROM movies WHERE movies.minutes > {min_length}
               ORDER by title ASC''')
    rows = db.fetchall()
    longer_than = [row[0] for row in rows]
    return longer_than
