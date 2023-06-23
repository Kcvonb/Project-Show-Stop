
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"
 
class Show(db.Model):

    __tablename__ = "shows"

    show_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    band = db.Column(db.String)
    description = db.Column(db.String)
    venue = db.Column(db.String)
    ticket_information = db.Column(db.String)
    poster_path = db.Column(db.String)


    def __repr__(self):
        return f"<Show show_id={self.show_id} title={self.title}>"


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
