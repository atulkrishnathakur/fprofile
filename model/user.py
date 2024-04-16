from database.dbconnection import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    country = Column(Integer)
    state = Column(Integer)
    city = Column(Integer)
    role = Column(Integer)
    zeep_code = Column(String)
    address = Column(String)
