from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from apis.router_base import api_router
from enum import Enum
from core.custom_exception import CustomException,unicorn_exception_handler
from core.jwtexception import JWTCustomException,jwterror_exception_handler
from database.repository.user import create_new_user
from middlewares.authchekermiddleware import AuthCheckerMiddleware

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()
app.add_exception_handler(CustomException,unicorn_exception_handler)
app.add_exception_handler(JWTCustomException,jwterror_exception_handler)
app.add_middleware(AuthCheckerMiddleware, some_attribute="example_attribute")