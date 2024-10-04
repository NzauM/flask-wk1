from flask import Flask, make_response,redirect, abort, request,jsonify
from models import db,Coffee,Order
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffeeshop.db'
db.init_app(app)
migrate = Migrate(app,db)


@app.route('/greet')
def welcome():
    resp_body = "<h1>Karibu Huku!!!</h1>"
    resp_code = 200
    headers = {"X-Api-Key":1234}
    resp = make_response(resp_body,resp_code,headers)
    return resp

@app.route('/logout')
def logout():
    return "<h3>You have been Logged Out</h3>",201

@app.route('/details/<student_name>')
def student_details(student_name):
    if student_name == "mercy":
        return redirect('/logout')
    elif student_name == "hope":
        abort(403)
    else:
        return f"<h1>Returning Details for {student_name}"
    
@app.route('/all-coffees')
def list_coffees():
    # get all coffees in our table
    all_cofis = Coffee.query.all()
    coffee_list = []
    # coffee_list = [cofi.to_dict() for cofi in all_cofis]
    for cofi in all_cofis:
        coffee_list.append(cofi.to_dict())
    resp_body = coffee_list
    resp_code = 200
    return make_response(resp_body,resp_code)

@app.route('/orders')
def list_orders():
    # get all orders
    # orders_list = []
    all_orders = Order.query.all()
    # for order in all_orders:
    #     order_dict = order.to_dict()
    #     orders_list.append(order_dict)
    # return make_response((orders_list),200)
    order_list = [order.to_dict() for order in all_orders]
    return make_response(order_list,200)

@app.route('/addcoffee',methods=['POST'])
def addCoffee():
    # receive data from request
    # use this data to create an instance
    # add this instance to session and commit it
    coffee_data = request.json
    print(coffee_data) #{'name': 'Black Coffee', 'price': 50.0}
    new_coffee = Coffee(name=coffee_data['name'], price=coffee_data['price'])
    db.session.add(new_coffee)
    db.session.commit()
    return make_response({'success':'New Coffee created'},201)










if __name__ == '__main__':
    app.run()

