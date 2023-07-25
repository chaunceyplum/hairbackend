from flask import Blueprint, request
from prisma.models import Barber
# import asyncio
from sqlalchemy import select
barber_blueprint = Blueprint('barber', __name__)

@barber_blueprint.route('/', methods=['GET','POST', 'DELETE'])
async def list_create ():
  if request.method == 'GET':
    barbers = await Barber.prisma().find_many()
    # result = session.execute(select(User).order_by(User.id))
    print(barbers)
    return {
      "data":  [barber.dict() for barber in barbers]
    }
  if request.method == 'POST':
    data = request.json

    if data is None:
      return {"error": "You need to fill in all fields accurately"}

    
    barberId = data.get('barberId')
    firstName = data.get('firstName')
    
    

    if firstName is None:
      return {"error": "You need to fill in all fields accurately"}

    

    barber = Barber.prisma().create(data={'firstName':firstName})

    return dict(barber),200
    # return barber dictionary

  if request.method == 'Delete':
    return
    