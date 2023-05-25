from flask import Flask
from prisma import Prisma, register
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from routes.customer import customer_blueprint
from routes.barber import barber_blueprint
from routes.appointment import appointment_blueprint
from routes.transaction import transaction_blueprint
import asyncio

# from sqlalchemy import create_engine
# engine = create_engine("postgres://gtfixtxgrbgrze:04ca58c50b220c61df03a4f4e9bcde65e3e31e596f7fcc91aa606429e3857c4a@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d8pqm4p4gon5th", echo=True)

# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# from routes.post import post_blueprint

db = Prisma()
db.connect()
register(db)





app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return {
    "Hello": "Welcome to the Hair Backend Server"
  }

app.register_blueprint(customer_blueprint, url_prefix='/customer')
app.register_blueprint(barber_blueprint, url_prefix='/barber')
app.register_blueprint(appointment_blueprint, url_prefix='/appointment')
app.register_blueprint(transaction_blueprint, url_prefix='/transaction')

if __name__ == "__main__":
  
  app.run(debug=True, port=5001, threaded=True)


