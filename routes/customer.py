from flask import Blueprint, request
from prisma.models import Customer

customer_blueprint = Blueprint('customer', __name__)

@customer_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'GET':
    customers = Customer.prisma().find_many(where={'customerId':True})
    return {
      "data": [Customer.dict() for customer in customers]
    }

  if request.method == 'POST':
    data = request.json

    if data is None:
      return
    
    customerId = data.get('customerId')
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    city = data.get('city')
    phoneNumber = data.get('phoneNumber')
    ffavoriteBarber = data.get('favoriteBarber')
    barber = data.get('barber')
    

    if phoneNumber is None or customerId is None:
      return {"error": "You need to fill in all fields accurately"}

    customer = Customer.prisma().create(data={'customerId': customerId, 'firstName': firstName, 'lastName': lastName, 'city': city, 'phoneNumber': phoneNumber, 'ffavoriteBarber':ffavoriteBarber,'barber':barber})

    return dict(customer)