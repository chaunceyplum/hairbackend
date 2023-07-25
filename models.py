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


class Base(DeclarativeBase):
     pass
class Appointment(Base):
   __tablename__ = "Appointment"
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
   barberId: Mapped[int] = mapped_column(primary_key=True)
   firstName: Mapped[str] = mapped_column(String(30))
   
 
   def __repr__(self) -> str:
       return f"Barber(barberId={self.barberId!r}, firstName={self.firstName!r})"
   
class Customer(Base):
   __tablename__ = "Customer"
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
   ContactId: Mapped[int] = mapped_column(primary_key=True)
   Name: Mapped[str] = mapped_column(String(30))
   Email: Mapped[str] = mapped_column(String(30), unique=True)
   Message: Mapped[str] = mapped_column(String(30))
   
   
   def __repr__(self) -> str:
       return f"Contact(contactId={self.appointmentId!r}, Name={self.Name!r},Email={self.Email!r},Message={self.Message!r}"
   