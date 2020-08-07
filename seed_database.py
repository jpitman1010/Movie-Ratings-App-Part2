"""Script to seed database."""

from flask_sqlalchemy import SQLAlchemy

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie.get('title')
    overview = movie.get('overview')
    poster_path = movie.get('poster_path')
    release_date_str = movie.get('release_date')
    # Example release date: "2020-05-22"
    release_date_format = "%Y-%m-%d"
    release_date = datetime.strptime(release_date_str, release_date_format)
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    # TODO: create a movie here and append it to movies_in_db
    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)

# Create users 1-10
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)

    # Create ratings 1-10 for each user
    for m in range(10):

        # make random score between 1-5
        score = randint(1,5)

        # get random movie
        random_movie = choice(movies_in_db)

        crud.create_rating(score, user, random_movie)
