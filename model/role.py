from database.dbconnection import Base
from sqlalchemy import Column, Integer, String

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)
