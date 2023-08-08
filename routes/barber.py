from flask import Blueprint, request, jsonify
# from prisma.models import Barber
import asyncio
from sqlalchemy import select
# from prisma import Client, register
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
# from app import db


barber_blueprint = Blueprint('barber', __name__)



class Base(DeclarativeBase):
     pass

class Barber(Base):
   __tablename__ = "Barber"
   __table_args__ = {'extend_existing': True}
   barberId: Mapped[int] = mapped_column(primary_key=True)
   firstName: Mapped[str] = mapped_column(String(30))
   
 
   def __repr__(self) -> str:
       return f"Barber(barberId={self.barberId!r}, firstName={self.firstName!r})"
   
@barber_blueprint.route('/', methods=['GET','POST', 'DELETE'])
def list_create ():
  
  if request.method == 'GET':
    # barbers =  Barber.prisma().find_many()
    # # result = session.execute(select(User).order_by(User.id))
    # print(barbers)
    # return {
    #   "data":  [barber.dict() for barber in barbers]
    # }


    # barbers = Barber.query.all()
    # barber_list = [{'id': barber.id, 'username': barber.username} for barber in barbers]
    # return jsonify(barber_list)



    barbers = select(Barber).where(Barber.firstName == 'Robert')
    result = db.session.execute(barbers)
    # return dict(barbers)
    return str(result)
  if request.method == 'POST':
    # data = request.json

    # if data is None:
    #   return {"error": "You need to fill in all fields accurately"}

    
    # barberId = data.get('barberId')
    # firstName = data.get('firstName')
    
    

    # if firstName is None:
    #   return {"error": "You need to fill in all fields accurately"}

    

    # barber = Barber.prisma().create(data={'firstName':firstName})

    # return dict(barber),200
    # # return barber dictionary
    return 'successfull https call'

  if request.method == 'Delete':
    return 'successfull https call'
    