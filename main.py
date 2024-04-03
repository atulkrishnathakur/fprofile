from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/fprofile_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

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

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String)

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String)
    country_id = Column(Integer)

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String)
    state_id = Column(Integer)
    country_id = Column(Integer)

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}