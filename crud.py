"""This module is responsible for CRUD operations in our Postgresql database"""

from model import db, connect_to_db, User, Movie, Rating

# functions below

def create_user(email, password):
    """Creates a new user object and returns it"""
    new_user = User(email=email, password=password)
    return new_user

def get_users():
    """Gets all users"""
    return User.query.all()

def get_user_by_id(user_id):
    """Gets user by id"""
    return User.query.get(user_id)

def create_movie(title, overview, release_date, poster_path):
    """Creates a new movie object and returns it"""
    new_movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    return new_movie

def get_movies(): #read
    """Return all movies from database"""
    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Gets movie by id"""
    return Movie.query.get(movie_id)

def create_rating(user, movie, score):
    """Creates a new rating object and returns it"""     
    new_rating = Rating(user=user, movie=movie, score=score)
    return new_rating

if __name__ == "__main__":
    from server import app
    connect_to_db(app)

