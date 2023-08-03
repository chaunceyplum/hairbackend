from flask import Blueprint, request
# from prisma.models import Appointment
import asyncio
# from prisma import Client, register
appointment_blueprint = Blueprint('appointment', __name__)

@appointment_blueprint.route('/', methods=['GET','POST'])
def list_create():
  

  if request.method == 'GET':
    # appointments =  Appointment.prisma().find_many()
    # return {
    #   "data": [appointment.dict() for appointment in appointments]
    # }
    return 'successfull https call'

  if request.method == 'POST':
    # data = request.json

    # if data is None:
    #  return {"error": "You need to fill in all fields accurately"}
    
    # appointmentId = data.get('appointmentId')
    # appointmentDate = data.get('appointmentDate')
    # Date = data.get('Date')
    # fcustomerId = data.get('fcustomerId')
    # fbarberId = data.get('fbarberId')
    
    

    # if appointmentId is None  or fbarberId is None or fcustomerId  is None or Date is None or appointmentDate is None:
    #   return {"error": "You need to fill in all fields accurately"}

    

    # # return dict(appointment)
   return 'successfull https call'