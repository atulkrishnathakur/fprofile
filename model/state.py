from database.dbconnection import Base
from sqlalchemy import Column, Integer, String

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String)
    country_id = Column(Integer)