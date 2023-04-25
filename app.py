from flask import Flask
from prisma import Prisma, register
from routes.customer import customer_blueprint
from routes.barber import barber_blueprint
from routes.appointment import appointment_blueprint
from routes.transaction import transaction_blueprint

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


