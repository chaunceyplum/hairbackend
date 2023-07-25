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
from prisma import Prisma
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import select
from prisma import Client, register

Base = automap_base()

app = Flask(__name__)
# engine = create_engine("postgresql://gtfixtxgrbgrze:04ca58c50b220c61df03a4f4e9bcde65e3e31e596f7fcc91aa606429e3857c4a@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d8pqm4p4gon5th", echo=True)
# Base.prepare(autoload_with=engine, reflect=True)


# session = Session(engine)



client = Client()
register(client)
asyncio.run( client.connect())
app.register_blueprint(customer_blueprint, url_prefix='/customer')
app.register_blueprint(barber_blueprint, url_prefix='/barber')
app.register_blueprint(appointment_blueprint, url_prefix='/appointment')
app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
@app.route('/', methods=['GET'])
def index():
  return {
    "Hello": "Welcome to the Hair Backend Server"
  }
# async def main() -> None:
#     db = Prisma(auto_register=True)
#     await db.connect()

#     # write your queries here
#     # barber = await db.barber.create(
#     #     data={
#     #         'firstName': 'Robert',
            
#     #     },
#     # )
#     # print(barber)

#     await db.disconnect()
@app.route("/barbers")
def user_list():
    barbers = session.execute(select(Barber).order_by(Barber.barberId))
    
    return dict(barbers)

if __name__ == "__main__":
  asyncio.run(main())
  # app.run(debug=True, port=5008, threaded=True)


