"""This module is responsible for CRUD operations in our Postgresql database"""

from model import db, connect_to_db, User, Movie, Rating

# functions below

def create_user(email, password):
    """Creates a new user object and returns it"""
    new_user = User(email=email, password=password)
    return new_user

def create_movie(title, overview, release_date, poster_path):
    """Creates a new movie object and returns it"""
    new_movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    return new_movie

def create_rating(user, movie, score):
    """Creates a new rating object and returns it"""     
    new_rating = Rating(user=user, movie=movie, score=score)
    return new_rating

if __name__ == "__main__":
    from server import app
    connect_to_db(app)

