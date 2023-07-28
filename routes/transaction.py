from flask import Blueprint, request
from prisma.models import Transaction
from datetime import datetime
import asyncio
from prisma import Client, register
transaction_blueprint = Blueprint('transaction', __name__)

@transaction_blueprint.route('/', methods=['GET','POST'])
def list_create():
  
  
  if request.method == 'GET':
    transactions = Transaction.prisma().find_many()
    return {
      "data": [transaction.dict() for transaction in transactions]
    }
    
  if request.method == 'POST':
    data = request.json

    if data is None:
      return
    
    transactionId = data.get('transactionId')
    fbarberId = data.get('fbarberId')
    fcustomerId = data.get('fcustomerId')
    # dateOfOrder = today
    orderPrice = data.get('orderPrice')
    

    if fbarberId is None or fcustomerId  is None or orderPrice is None:
      return  "You need to fill in all fields accurately", 500

    transaction = Transaction.prisma().create(data={'transactionId':transactionId,'fbarberId': fbarberId, 'fcustomerId': fcustomerId,  'orderPrice': orderPrice})

  return dict(transaction),200
    



  #model data
  # {
    
  #   "fbarberId":1,
  #   "fcustomerId":"1",
  #   "orderPrice":"30"
    
  # }