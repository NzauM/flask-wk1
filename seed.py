# create instances of our class
# add the instance to our db/SQLAlchemy instance session
# commit the session
from models import Coffee,db
from app import app
from faker import Faker
import random

fake = Faker()

with app.app_context():
    coffees = [Coffee(name=fake.unique.name(), price=(random.randint(5,100)+0.50)) for i in range(10)]

    db.session.add_all(coffees)
    db.session.commit()
    print("Coffees Seeded")




