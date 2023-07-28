from flask import Blueprint, request
from prisma.models import Customer
import asyncio
from prisma import Client, register
customer_blueprint = Blueprint('customer', __name__)

@customer_blueprint.route('/', methods=['GET','POST'])
def list_create():
  
  if request.method == 'GET':
    customers =  Customer.prisma().find_many()
    return {
      "data": [customer.dict() for customer in customers]
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
    ffavoriteBarber = data.get('ffavoriteBarber')
      
    

    if phoneNumber is None or customerId is None or firstName is None:
      return {"error": "You need to fill in all fields accurately"}

    customer = Customer.prisma().create(data={'customerId': customerId, 'firstName': firstName, 'lastName': lastName, 'city': city, 'phoneNumber': phoneNumber, 'ffavoriteBarber':ffavoriteBarber})

    return dict(customer)
    
  
# {
#     "customerId":"1",
#     "firstName":"Chauncey",
#     "lastName":"Plummer",
#     "city":"Queens",
#     "phoneNumber":19293732368,
#     "ffavoriteBarber":1
    
#   }