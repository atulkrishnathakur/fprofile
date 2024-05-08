from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from apis.router_base import api_router
from enum import Enum
from core.custom_exception import CustomException
from fastapi.responses import JSONResponse, ORJSONResponse
from database.repository.user import create_new_user


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()


@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status_code":exc.status_code,"status":exc.status,"message":exc.message,"data":exc.data},
    )