"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect

from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "super secret"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route("/")
def homepage():
    """View Home Page"""
    return render_template("homepage.html")

@app.route("/movies")
def all_movies():
    """A view for all of the movies."""
    movies = crud.get_movies()
    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show the info about a specific movie"""
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)

@app.route("/users", methods=["GET"])
def all_users():
    """View for all users"""
    users = crud.get_users()
    return render_template("all_users.html", users=users)

@app.route("/users", methods=["POST"])
def register_user():
    """Creates a new users"""
    new_email = request.form["email"]
    new_password = request.form["password"]

    user = crud.get_user_by_email(new_email)
    
    if user:
        flash("Cannot create an account with that email. Try again.") 
    else:
        new_user = crud.create_user(new_email, new_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account has been created")

    return redirect("/")

@app.route("/users/<user_id>")
def show_user(user_id):
    """"Show specific user id"""
    user = crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    """Where a user goes once they log in"""
    email = request.form["email"]
    password = request.form["password"]

    user = crud.get_user_by_email(email)

    if user:
        session["user_email"] = user.email
        flash(f"Successfully logged in as {user.email}")
    else:
        flash("This email is not registered")

    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)
