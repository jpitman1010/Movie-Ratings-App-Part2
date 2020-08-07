"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """get a list of all users"""

    return db.session.query(User).all()

def get_user_by_id(user_id):
    """Return the user object by ID"""

    return db.session.query(User).filter_by(user_id=user_id).one()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview,release_date=release_date,poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """Returns a list of all movies in database"""

    return db.session.query(Movie).all()


def get_movie_by_id(movie_id):
    """Return movie with that id"""

    return db.session.query(Movie).filter_by(movie_id=movie_id).one()


def create_rating(score, user, movie):
    """Create a rating"""

    rating = Rating(score=score, user=user, movie=movie)

    db.session.add(rating)
    db.session.commit()

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)