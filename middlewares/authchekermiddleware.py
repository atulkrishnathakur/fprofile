from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse, ORJSONResponse, HTMLResponse
from fastapi import Depends, status, HTTPException, Request, Header
from apis.router_base import api_router

class AuthCheckerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, some_attribute: str):
        super().__init__(app)
        self.some_attribute = some_attribute
    # url_path_for("route name here")
    async def dispatch(self, request: Request, call_next):
        excluded_paths = [
            "/docs",
            "/openapi.json",
            api_router.url_path_for("login"),
            api_router.url_path_for("test")
            ]
        if request.url.path not in excluded_paths and not request.headers.get("ACCESS-TOKEN"):
            return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "You have need to login first", "message": "login first","token":str(request.headers.get("ACCESS-TOKEN"))},
            )   
        response = await call_next(request)
        return response