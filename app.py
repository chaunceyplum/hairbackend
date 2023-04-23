from flask import Flask
from prisma import Prisma, register
from routes.customer import customer_blueprint
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
# app.register_blueprint(post_blueprint, url_prefix='/post')

if __name__ == "__main__":

  app.run(debug=True, port=5000, threaded=True)