from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import asyncio
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin


db = SQLAlchemy()
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "https://classycutz.netlify.app", "allow_headers": "*", "expose_headers": "*"}})

     #,origins=['http://localhost',"https://classycutz.netlify"])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gtfixtxgrbgrze:04ca58c50b220c61df03a4f4e9bcde65e3e31e596f7fcc91aa606429e3857c4a@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d8pqm4p4gon5th'

db.init_app(app)

#app.config['CORS_HEADERS'] = 'Content-Type'



def main() -> None:
  with app.app_context():
    db.reflect()
print(dict(db.metadatas))

class Appointment(db.Model):
    __tablename__ = "Appointment"
    __table_args__ = {'extend_existing': True}
    appointmentid = sa.Column(sa.Integer, primary_key=True)
    fcustomerId = sa.Column(sa.Integer)
    fbarberId = sa.Column(sa.Integer)
    Date = sa.Column(sa.DateTime)
    appointmentDate = sa.Column(sa.DateTime)
    firstname = sa.Column(sa.String)

appointment_table =db.Table(
    "Appointment",
    appointmentid = sa.Column(sa.Integer, primary_key=True),
    fcustomerId = sa.Column(sa.Integer),
    fbarberId = sa.Column(sa.Integer),
    Date = sa.Column(sa.DateTime),
    appointmentDate = sa.Column(sa.DateTime),
    firstname = sa.Column(sa.String)
)

class Barber(db.Model):
    __tablename__ = "Barber"
    __table_args__ = {'extend_existing': True}
    barberid = sa.Column(sa.Integer, primary_key=True)
    firstname = sa.Column(sa.String)

barber_table = db.Table(
    "Barber",
    barberid = sa.Column(sa.Integer, primary_key=True),
    firstname = sa.Column(sa.String),
)

class Customer(db.Model):
  __tablename__ = "Customer"
  __table_args__ = {'extend_existing': True}
  customerId  = sa.Column(sa.Integer, primary_key=True)
  firstname = sa.Column(sa.String)
  lastname = sa.Column(sa.String)
  city = sa.Column(sa.String)
  phonenumber = sa.Column(sa.String)
  ffavoriteBarber =sa.Column(sa.Integer)
  email = sa.Column(sa.String)
  password = sa.Column(sa.String)
  isLoggedIn =  sa.Column(sa.Boolean, default=False)
  is_authenticated = sa.Column(sa.Boolean, default=False)
  is_active = sa.Column(sa.Boolean, default=False)
  is_anonymous = sa.Column(sa.Boolean, default=True)

  def get_id(self):
    return self.email

customer_table = db.Table(
  "Customer",
  customerId  = sa.Column(sa.Integer, primary_key=True),
  firstName = sa.Column(sa.String),
  lastName = sa.Column(sa.String),
  city = sa.Column(sa.String),
  phoneNumber = sa.Column(sa.String),
  ffavoriteBarber =sa.Column(sa.Integer),
  email = sa.Column(sa.String),
  password = sa.Column(sa.String),
  isLoggedIn =  sa.Column(sa.Boolean, default=False),
  is_authenticated = sa.Column(sa.Boolean, default=False),
  is_active = sa.Column(sa.Boolean, default=False),
  is_anonymous = sa.Column(sa.Boolean, default=True),
)

class Transaction(db.Model):
  __tablename__ = "Transaction"
  __table_args__ = {'extend_existing': True}
  transactionId = sa.Column(sa.Integer, primary_key=True)
  fcustomerId = sa.Column(sa.Integer)
  orderPrice =sa.Column(sa.Integer)
  fbarberId = sa.Column(sa.Integer)
  Date = sa.Column(sa.DateTime)

transaction_table = db.Table(
  "Transaction",
  transactionId = sa.Column(sa.Integer, primary_key=True),
  fcustomerId = sa.Column(sa.Integer),
  orderPrice =sa.Column(sa.Integer),
  fbarberId = sa.Column(sa.Integer),
  Date = sa.Column(sa.DateTime)
)


@app.route('/')
@cross_origin()
def index():
  return {"status":"up"}

@app.after_request
def after_request(response):
  #response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response


@app.route('/login/', methods=['POST'])
@cross_origin()
def login_customer():
  data = request.json
  email = data["data"]["email"]
  unhashedPassword = data["data"]["password"]
  password = generate_password_hash(unhashedPassword)
 
  if email is None:
    return {"error": "You need to fill in all fields accurately"}

  customer = db.session.execute(db.select(Customer).filter_by(email=email)).scalar_one()

  if customer is None:
    return {"error":"Email does not exist"}

  databasePass = customer.password
  print(databasePass)
  
  if databasePass != password:
    return {"error":"password does not match"}
  

  print(customer)
  return {customer},200
    
@app.route('/getAppointments', methods=['GET'])
@cross_origin()
def Appointment_list():
  Appointments = text('SELECT * FROM public."Appointment"')
  
  result = db.session.execute(Appointments)
  result1 =result.mappings().all()
  result2 = "{" + f'"data":{result1}' +"}"
  
  print(result2)
  return str(result2)      

    
    
@app.route('/getBarbers', methods=['GET'])
@cross_origin()
def barber_list():
  barbers = text('SELECT * FROM public."Barber"')
  
  result = db.session.execute(barbers)
  result1 =result.mappings().all()
  result2 = "{" + f'"data":{result1}' +"}"
  
  print(result2)
  return str(result2)

@app.route('/addBarbers', methods=['POST'])
@cross_origin()
def add_barber():
  data = request.json
  # if data is None:
  #   return {"error": "You need to fill in all fields accurately"}
  barbers = text('SELECT * FROM public."Barber"')
  result = db.session.execute(barbers)
  result1 =result.mappings().all()
  newId = len(result1) + 1 
  firstname = data["data"]["firstname"]
  print(data)
  if firstname is None:
    return {"error": "You need to fill in all fields accurately"}

  barber = Barber(barberid=f'{newId}', firstname=f'{firstname}')
  db.session.add(barber)
  db.session.commit()

  print(barber)
  return str(f'record: {barber}, inserted successfully '),200
 
@app.route('/getTransactions', methods=['GET'])
@cross_origin()
def Transaction_list():
  barbers = text('SELECT * FROM public."Transaction"')
  
  result = db.session.execute(barbers)
  result1 =result.mappings().all()
  result2 = "{" + f'"data":{result1}' +"}"
  
  print(result2)
  return str(result2)

@app.route('/addTransaction', methods=['POST'])
@cross_origin()
def add_transaction():
  data = request.json
  # if data is None:
  #   return {"error": "You need to fill in all fields accurately"}
  transactions = text('SELECT * FROM public."Transaction"')
  result = db.session.execute(transactions)
  result1 =result.mappings().all()
  newId = len(result1) + 1 
  customerId = data["data"]["customerId"]
  orderPrice = data["data"]["orderPrice"]
  fbarberId = data["data"]["fbarberId"]
  Date = data["data"]["Date"]
  

  print(data)
  if data is None:
    return {"error": "You need to fill in all fields accurately"}

  transaction = Transaction(transactionId=f'{newId}', customerId=f'{customerId}',orderPrice=f'{orderPrice}',fbarberId=f'{fbarberId}',Date=f'{Date}')
  db.session.add(transaction)
  db.session.commit()

  print(transaction)
  return str(f'record: {transaction}, inserted successfully '),200

@app.route('/getCustomers', methods=['GET'])
@cross_origin()
def Customer_list():
  barbers = text('SELECT * FROM public."Customer"')
  
  result = db.session.execute(barbers)
  result1 =result.mappings().all()
  result2 = "{" + f'"data":{result1}' +"}"
  
  print(result2)
  return str(result2)

@app.route('/addCustomer', methods=['POST'])
@cross_origin()
def add_customer():
  data = request.json
  # if data is None:
  #   return {"error": "You need to fill in all fields accurately"}

  customers = text('SELECT * FROM public."Customer"')
  result = db.session.execute(customers)
  result1 =result.mappings().all()
  newId = len(result1) + 1 
  firstname = data["data"]["firstname"]
  lastname = data["data"]["lastname"]
  city = data["data"]["city"]
  phonenumber = data["data"]["phonenumber"]
  ffavoriteBarber = data["data"]["ffavoriteBarber"]
  email = data["data"]["email"]
  unhashedPassword = data["data"]["password"]
  password = generate_password_hash(unhashedPassword)
  # isloggedin = data["data"]["isloggedin"]
  # is_authenticated = data["data"]["is_authenticated"]
  # is_active = data["data"]["is_active"]
  # is_anonymous = data["data"]["is_anonymous"]

  print(data)
  if firstname is None:
    return {"error": "You need to fill in all fields accurately"}

  customer = Customer(customerId=f'{newId}', firstname=f'{firstname}',lastname=f'{lastname}',city=f'{city}',phonenumber=f'{phonenumber}',ffavoriteBarber=f'{ffavoriteBarber}',email=f'{email}',password = f"{password}")
  db.session.add(customer)
  db.session.commit()

  print(customer)
  return str(f'record: {customer}, inserted successfully '),200


if __name__ == '__main__':
  main()
