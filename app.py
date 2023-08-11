from flask import Flask, jsonify
# from prisma import Prisma, register
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from routes.customer import customer_blueprint
from routes.barber import barber_blueprint
from routes.appointment import appointment_blueprint
from routes.transaction import transaction_blueprint
from routes.login import login_blueprint
import asyncio
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

import datetime
from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy import select
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# from flask_cors import CORS
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gtfixtxgrbgrze:04ca58c50b220c61df03a4f4e9bcde65e3e31e596f7fcc91aa606429e3857c4a@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d8pqm4p4gon5th'




db.init_app(app)



# engine = create_engine('postgresql://gtfixtxgrbgrze:04ca58c50b220c61df03a4f4e9bcde65e3e31e596f7fcc91aa606429e3857c4a@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d8pqm4p4gon5th')
# # Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)
# session = Session()
class Barber(db.Model):
    __tablename__ = "Barber"
    __table_args__ = {'extend_existing': True}
    barberId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, unique=True, nullable=False)
def main() -> None:
  with app.app_context():
    db.create_all()

# class Transaction:
#     __table__ = db.metadatas["auth"].tables["Transaction"]
# class Barber:
#     __table__ = db.metadatas["auth"].tables["Barber"]
# class Customer:
#     __table__ = db.metadatas["auth"].tables["Customer"]
# class Appointment:
#     __table__ = db.metadatas["auth"].tables["Appointment"]

  
# app.register_blueprint(customer_blueprint, url_prefix='/customer')
# app.register_blueprint(barber_blueprint, url_prefix='/barber')
# app.register_blueprint(appointment_blueprint, url_prefix='/appointment')
# app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
# app.register_blueprint(login_blueprint, url_prefix='/login')

# @app.route('/barber')
# def get_barber():
#   barbers = select(Barber).where(Barber.firstName == 'Robert')
#   result = session.execute(barbers)
#   # return dict(barbers)
#   return str(result)

@app.route('/')
def index():
  # return {"status":"up"}
    barbers = text('SELECT * FROM public."Barber"')
    
    result = db.session.execute(barbers)
    result1 =result.mappings().all()
    result2 = "{" + f'"data":{result1}' +"}"
    
    print(result2)
    return str(result2)

    for row in result1:
      #  return row["Object"].name
      return str(row)
      

    
    
@app.route('/barber')
def user_list():
    sql = text('SELECT * FROM public."Barber"')
 
    with db.engine.begin() as conn:
        response = conn.exec_driver_sql(sql)
    
    return response
    


  
  # db = Prisma()
  # db.connect()

  # # write your queries here

  # db.disconnect()
 


if __name__ == '__main__':
  main()
