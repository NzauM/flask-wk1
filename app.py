from flask import Flask, make_response,redirect, abort, request
from models import db,Coffee
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
        





if __name__ == '__main__':
    app.run()

