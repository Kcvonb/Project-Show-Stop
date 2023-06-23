
from model import Show, db, User, Movie, Rating, connect_to_db


def create_user(email, password):

    user = User(email=email, password=password)

    return user


def get_users():

    return User.query.all()


def get_user_by_id(user_id):

    return User.query.get(user_id)


def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


# def create_show(band, description, venue, ticket_information, poster_path):
    
#     show = Show(
#         band=band,
#         description=description,
#         venue=venue,
#         ticket_information=ticket_information
#         poster_path=poster_path,
#     )

#     return show


def get_movies():
    """Return all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Return a movie by primary key."""

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating


def update_rating(rating_id, new_score):
    """ Update a rating given rating_id and the updated score. """
    rating = Rating.query.get(rating_id)
    rating.score = new_score

if __name__ == "__main__":
    from server import app

    connect_to_db(app)

