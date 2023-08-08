from flask import Flask, jsonify
# from prisma import Prisma, register
from flask import Flask, render_template, request, url_for, redirect
from routes.customer import customer_blueprint
from routes.barber import barber_blueprint
from routes.appointment import appointment_blueprint
from routes.transaction import transaction_blueprint
from routes.login import login_blueprint
import asyncio
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
# from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gtfixtxgrbgrze:04ca58c50b220c61df03a4f4e9bcde65e3e31e596f7fcc91aa606429e3857c4a@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d8pqm4p4gon5th'
db = SQLAlchemy(app)


class Base(DeclarativeBase):
     pass
class Appointment(Base):
   __tablename__ = "Appointment"
   __table_args__ = {'extend_existing': True}
   appointmentId: Mapped[int] = mapped_column(primary_key=True)
   fcustomerId: Mapped[int] 
   fbarberId: Mapped[int] 
   date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
   appointmentDate: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
   phoneNumber: Mapped[int] = mapped_column(unique=True)
   
   def __repr__(self) -> str:
       return f"Appointment(appointmentId={self.appointmentId!r}, fcustomerId={self.fcustomerId!r},fbarberId={self.fbarbererId!r},date={self.date!r},appointmentDate={self.appointmentDate!r},phoneNumber={self.phoneNumber!r})"
   
class Barber(Base):
   __tablename__ = "Barber"
   __table_args__ = {'extend_existing': True}
   barberId: Mapped[int] = mapped_column(primary_key=True)
   firstName: Mapped[str] = mapped_column(String(30))
   
 
   def __repr__(self) -> str:
       return f"Barber(barberId={self.barberId!r}, firstName={self.firstName!r})"
   
class Customer(Base):
   __tablename__ = "Customer"
   __table_args__ = {'extend_existing': True}
   customerId: Mapped[int] = mapped_column(primary_key=True)
   firstName: Mapped[str] = mapped_column(String(30))
   lastName: Mapped[str] = mapped_column(String(30))
   city: Mapped[str] = mapped_column(String(30))
   phoneNumber: Mapped[str] = mapped_column(String(30))
   ffavoriteBarber: Mapped[str] = mapped_column(String(30))
   email: Mapped[str] = mapped_column(String(30))
   password: Mapped[str] = mapped_column(String(30))
   isLoggedIn: Mapped[bool]  
   # addresses: Mapped[List["Address"]] = relationship(
   #     back_populates="user", cascade="all, delete-orphan"
   # )
   def __repr__(self) -> str:
       return f"Customer(customerId={self.customerId!r}, firstName={self.firstName!r},lastName={self.lastName!r},city={self.city!r},phoneNumber={self.phoneNumber!r},ffavoriteBarber={self.ffavoriteBarber!r},email={self.email!r},password={self.password!r}, isLoggedIn={self.isLoggedIn!r})"
   
class Transaction(Base):
   __tablename__ = "Transaction"
   __table_args__ = {'extend_existing': True}
   transactionId: Mapped[int] = mapped_column(primary_key=True)
   fcustomerId: Mapped[int] = mapped_column(unique=True)
   orderPrice: Mapped[int] = mapped_column(unique=True)
   fbarberId: Mapped[int] = mapped_column(unique=True)
   Date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
   # addresses: Mapped[List["Address"]] = relationship(
   #     back_populates="user", cascade="all, delete-orphan"
   # )
   def __repr__(self) -> str:
       return f"Transaction(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Contact(Base):
   __tablename__ = "Appointment"
   __table_args__ = {'extend_existing': True}
   ContactId: Mapped[int] = mapped_column(primary_key=True)
   Name: Mapped[str] = mapped_column(String(30))
   Email: Mapped[str] = mapped_column(String(30), unique=True)
   Message: Mapped[str] = mapped_column(String(30))
   
   
   def __repr__(self) -> str:
       return f"Contact(contactId={self.appointmentId!r}, Name={self.Name!r},Email={self.Email!r},Message={self.Message!r}"
   
app.register_blueprint(customer_blueprint, url_prefix='/customer')
# app.register_blueprint(barber_blueprint, url_prefix='/barber')
app.register_blueprint(appointment_blueprint, url_prefix='/appointment')
app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
app.register_blueprint(login_blueprint, url_prefix='/login')

@app.route('/barber', methods=['GET'])
def get_barber():
  barbers = select(Barber).where(Barber.firstName == 'Robert')
  result = db.session.execute(barbers)
  # return dict(barbers)
  return str(result)
@app.route('/')
def index():
    return {'status':'up'}

def main() -> None:
  
  # db = Prisma()
  # db.connect()

  # # write your queries here

  # db.disconnect()
  blah = 1


if __name__ == '__main__':
  main()
