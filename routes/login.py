from flask import Blueprint, request
from prisma.models import Customer
import asyncio
from sqlalchemy import select
from prisma import Client, register
from flask import Flask, jsonify

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/', methods=['POST'])
async def list_create ():
  # s
  # if request.method == 'GET':
  #   # logins =  login.prisma().find_many()
  #   # # result = session.execute(select(User).order_by(User.id))
  #   # print(logins)
  #   # return {
  #   #   "data":  [login.dict() for login in logins]
  #   # }
  #   print('youve reachec the logins page')
  if request.method == 'POST':
    data = request.json

    data1 = data['data'] 
 # jnm,
    
    email = data1['email']
    # email1 = data1.data 
    password = data1['password']
    # print(data['data'])
    if data is None:
     return 500

    if email is None:
      return {"error": "You need to fill in email accurately"},500

    if password is None:
      return {"error": "You need to fill in password accurately"},500

    login = Customer.prisma().find_first(where={'email':{'contains':email}})

    return dict(login),200
    # return login dictionary
  else:
    return 500
  # if request.method == 'Delete':
  #   return



    