"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies"""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    """View details about one movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def get_list_of_users():
    """View List of Users"""

    users = crud.get_users()

    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def get_user_profile(user_id):
    """View user profile details"""
    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

