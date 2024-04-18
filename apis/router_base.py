from apis.routers import user_route
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(user_route.router, prefix="", tags=["users"])