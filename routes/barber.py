from flask import Blueprint, request
from prisma.models import Barber
import asyncio

barber_blueprint = Blueprint('barber', __name__)

@barber_blueprint.route('/', methods=['GET','POST', 'DELETE'])
async def list_create():
  if request.method == 'GET':
    barbers = Barber.prisma().find_many()
    return {
      "data": [barber.dict() for barber in barbers]
      
    }

  if request.method == 'POST':
    data = request.json

    if data is None:
      return
    
    barberId = data.get('barberId')
    firstName = data.get('firstName')
    
    

    if firstName is None or barberId is None:
      return {"error": "You need to fill in all fields accurately"}

    barber = Barber.prisma().create(data={'barberId': barberId, 'firstName': firstName})

    return dict(barber)
    # return barber

  if request.method == 'Delete':
    barber = await Barber.prisma().delete_many()
    