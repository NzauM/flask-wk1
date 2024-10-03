from app import app
from models import db,Coffee, Customer, Order
from faker import Faker
import random

fake = Faker()

with app.app_context():

    Coffee.query.delete()
    Customer.query.delete()
    Order.query.delete()
    print("Cleared Tables")

    coffees = [Coffee(name=fake.word(), price=random.randint(5,100)+0.50) for i in range(10)]
    db.session.add_all(coffees)
    db.session.commit()
    print("Seeded 10 Coffeezs")

    customers = [Customer(name=fake.name(), phone_no=fake.phone_number()) for i in range(10)]
    db.session.add_all(customers)
    db.session.commit()
    print("Seeded 10 Customerss")

    orders = [Order(customer_id=random.randint(1,10), coffee_id=random.randint(1,10)) for i in range(10)]
    db.session.add_all(orders)
    db.session.commit()
    print("Seeded 10 Orders")



    # for i in range(10):
    #     coffee = Coffee(name=fake.word(), price=random.randint(5,100)+0.50)

