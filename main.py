from fastapi import FastAPI,Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from apis.router_base import api_router
from enum import Enum

from database.repository.user import create_new_user


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = app = FastAPI()
    include_router(app)
    return app

app = start_application()
