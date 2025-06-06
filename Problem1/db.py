#Edward Yeboah
#CSE 337 HW 5
#SBU ID: 114385084

import sys
import os
import sqlite3
from contextlib import closing

from objects import Category
from objects import Movie

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = os.path.join(os.path.dirname(__file__), "movies.db")
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():    
    if conn:
        conn.close()

def make_category(row):
    return Category(row["categoryID"], row["categoryName"])

def make_movie(row):
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"],
            make_category(row))

def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            return make_category(row)
        else:
            return None

def get_movies_by_category(category_id):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_movies_by_minutes():
    minutes = int(input("Minutes: "))
    query = ''' SELECT movieID, Movie.name, year, minutes,
    Movie.categoryID as categoryID, Category.name as categoryName
    FROM Movie JOIN Category
    ON Movie.categoryID = Category.categoryID
    WHERE minutes = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (minutes,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies
  

def get_movie():
    movie = input("Movie: ")
    query = ''' SELECT movieID, Movie.name, year, minutes,
    Movie.categoryID as categoryID, Category.name as categoryName
    FROM Movie JOIN Category
    ON Movie.categoryID = Category.categoryID
    WHERE name = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (movie,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

    

def add_movie(movie):
    query = '''SELECT * FROM Movie WHERE name = ? AND year = ? AND minutes = ? AND categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (movie.name, movie.year, movie.minutes, movie.category.id))
        if c.fetchone() != None:
            print("Movie already exists")
            return 
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()

def delete_movie(movie_id):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        test = conn.commit()
        print("Test", test)
