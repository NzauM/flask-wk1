from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy


db = SQLAlchemy()

class Coffee(db.Model, SerializerMixin):
    # A Coffee has many orders

    __tablename__ = 'coffees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    orders = db.relationship('Order',back_populates='coffee')
    customers = association_proxy('orders','customer', creator=lambda coffeeObj: Order(coffee = coffeeObj))


class Customer(db.Model,SerializerMixin):
    # A customer has many orders
    # A cofee can have many customers by making many orders
    # So Customer has Many Coffees through Orders

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone_no = db.Column(db.String)

    orders = db.relationship('Order',back_populates='customer')

    coffees = association_proxy('orders','coffee', creator=lambda thisInstance: Order(customer = thisInstance))

    # coffees = [order.coffee for order in allOrders where order.customer = thiscustomer]


class Order(db.Model,SerializerMixin):

    # An order belongs to a customer
    # An order belongs to a coffee

    __tablename__ = 'orders'
    serialize_rules = ("-customer.orders",'-coffee.orders')
    # serialize_only=('customer_id','coffee')
    

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffees.id'))

    customer = db.relationship('Customer',back_populates='orders')
    coffee = db.relationship('Coffee',back_populates = 'orders')

# /orders/1
# The first order
# {
#     "id":1,
#     "customer_id":1,
#     "coffee_id":1,
#     "customer":{
#         "id":1,
#         "name":"Mercy",
#         "phone_no":789,
#         "orders":[{
#             "id":1,
#             "customer_id":1,
#             "coffee_id":1
#             "customer":{
#                 "id"
#                 "name"
#                 "phone_no"
#                 "coffees":[]
#             }

#         }]
#     }

# }
