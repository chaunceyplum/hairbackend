from flask import Blueprint, request
from prisma.models import Transaction

transaction_blueprint = Blueprint('transaction', __name__)

@transaction_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'GET':
    transactions = Transaction.prisma().find_many(where={'transactionId':True})
    return {
      "data": [transaction.dict() for transaction in transactions]
    }

  if request.method == 'POST':
    data = request.json

    if data is None:
      return
    
    transactionId = data.get('transactionId')
    fbarberId = data.get('firstName')
    fcustomerId = data.get('lastName')
    dateOfOrder = data.get('city')
    orderPrice = data.get('phoneNumber')
    
    

    if transactionId is None  or fbarberId is None or fcustomerId  is None or dateOfOrder is None or orderPrice is None:
      return {"error": "You need to fill in all fields accurately"}

    transaction = Transaction.prisma().create(data={'transactionId': transactionId, 'fbarberId': fbarberId, 'fcustomerId': fcustomerId, 'dateOfOrder': dateOfOrder, 'orderPrice': orderPrice})

    return dict(transaction)