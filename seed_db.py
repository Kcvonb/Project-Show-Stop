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

shows_in_db = []
for Show in show_data:
    band, description, venue, ticket, infomation, poster_path = (
        Show["band"],
        Show["description"],
        Show["venue"],
        Show["ticket information"]
    )

    db_movie = crud.create_movie(band, description, venue, ticket, infomation, poster_path)
    shows_in_db.append(db_show)

model.db.session.add_all(shows_in_db)
model.db.session.commit()   

for n in range(10):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)


model.db.session.commit()
