import sqlalchemy as sa
from app import db 
class Barber(db.Model):
    __tablename__ = "Barber"
    __table_args__ = {'extend_existing': True}
    id = sa.Column(sa.Integer, primary_key=True)
    type = sa.Column(sa.String)