from flask import Blueprint, request
from prisma.models import Appointment

appointment_blueprint = Blueprint('appointment', __name__)

@appointment_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'GET':
    appointments = Appointment.prisma().find_many(where={'appointmentId':True})
    return {
      "data": [Appointment.dict() for appointment in appointments]
    }

  if request.method == 'POST':
    data = request.json

    if data is None:
      return
    
    appointmentId = data.get('appointmentId')
    appointmentDate = data.get('appointmentDate')
    Date = data.get('Date')
    fcustomerId = data.get('fcustomerId')
    fbarberId = data.get('fbarberId')
    
    

    if appointmentId is None  or fbarberId is None or fcustomerId  is None or dateOfOrder is None or orderPrice is None:
      return {"error": "You need to fill in all fields accurately"}

    appointment = Appointment.prisma().create(data={'appointmentId': appointmentId, 'fbarberId': fbarberId, 'fcustomerId': fcustomerId, 'date': Date, 'appointmentDate': appointmentDate})

    return dict(appointment)