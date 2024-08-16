from apis.routers import user_route
from apis.routers import login_route
from apis.routers import mail_route
from fastapi import APIRouter, FastAPI

api_router = APIRouter()
api_router.include_router(user_route.router, prefix="", tags=["users"])
api_router.include_router(login_route.router, prefix="", tags=["Login"])
api_router.include_router(mail_route.router, prefix="", tags=["Mail"])