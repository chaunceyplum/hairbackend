# from flask import Flask
from prisma import Prisma, register
from flask import Flask, render_template, request, url_for, redirect
from routes.customer import customer_blueprint
from routes.barber import barber_blueprint
from routes.appointment import appointment_blueprint
from routes.transaction import transaction_blueprint
from routes.login import login_blueprint
import asyncio

from prisma import Client, register
import prisma

# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# prisma.register(prisma.Prisma())
# prisma.connect()

client = Client()
register(client)
client.connect()

# db = Prisma()
# db.connect()


app.register_blueprint(customer_blueprint, url_prefix='/customer')
app.register_blueprint(barber_blueprint, url_prefix='/barber')
app.register_blueprint(appointment_blueprint, url_prefix='/appointment')
app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
app.register_blueprint(login_blueprint, url_prefix='/login')

@app.route('/')
def index():
    return {'status':'up'}

def main() -> None:
  db = Prisma()
  db.connect()

  # write your queries here

  db.disconnect()

if __name__ == '__main__':
  main()
