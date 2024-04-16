from database.dbconnection import Base
from sqlalchemy import Column, Integer, String

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String)
    state_id = Column(Integer)
    country_id = Column(Integer)