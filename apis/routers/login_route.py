from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.session import get_db
from core.hashing import HashData
from core.config import settings
from core.security import create_access_token, blacklist
from core.message import message
from core.constants import constants
from core.auth import authenticate_user, get_current_active_user
from core.custom_exception import CustomException
from core.apikeyheader import header_scheme
from core.logger import logger
from database.repository.login import get_user
from schema.token import Token, TokenData, TokenCredentialIn,TokenOut, Logout
from schema.user import UserSchemaOut, BaseUserSchema
from fastapi.responses import JSONResponse, ORJSONResponse
from fastapi.security import APIKeyHeader
from core.auth import get_current_user
from core.logger import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("/login",response_model=TokenOut, response_class=JSONResponse,name="login")
async def login_for_access_token(credentials: TokenCredentialIn,db:Session = Depends(get_db)):
    user = authenticate_user(credentials.email, credentials.password,db)
    if not user:
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=constants.STATUS_UNAUTHORIZED,
            message=message.INCORRECT_CREDENTIALS,
            data=[]
        )
    elif(user.is_active == False):
        raise CustomException(status_code=status.HTTP_403_FORBIDDEN,status=constants.STATUS_FORBIDDEN,message=message.INACTIVE_USER,data=[])  

    access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    http_status_code: int = status.HTTP_200_OK
    user_data = {
        "status_code": http_status_code,
        "status":constants.STATUS_OK,
        "access_token":access_token,
        "token_type":settings.TOKEN_TYPE,
        "first_name": user.first_name,
        "email": user.email,
        "role": user.role,
        "country":user.country,
        "state":user.state,
        "city":user.city,
        "address":user.address,
        "zeep_code":user.zeep_code
    }
    response_data = TokenOut(**user_data)
    response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
    return response
    
@router.get("/users/me/", response_model=UserSchemaOut)
async def read_users_me(current_user: Annotated[UserSchemaOut, Depends(get_current_active_user)]):
    http_status_code: int = status.HTTP_200_OK
    status_ok:bool = constants.STATUS_OK
    data = {"status_code":http_status_code,"status":status_ok,"first_name":current_user.first_name,"last_name":current_user.last_name,"email":current_user.email,"username":current_user.username,"role":current_user.role,"country":current_user.country,"state":current_user.state,"city":current_user.city,"address":current_user.address,"zeep_code":current_user.zeep_code}
    response_data = UserSchemaOut(**data)
    response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
    return response

@router.post("/logout", response_model=Logout)
async def logout(token: Annotated[str, Depends(header_scheme)]):
    blacklist.add(token)
    http_status_code: int = status.HTTP_200_OK
    status_ok:bool = constants.STATUS_OK
    data={"status_code":http_status_code,"status":status_ok,"message":message.LOGOT_SUCCESS}
    response_data = Logout(**data)
    response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
    return response
@router.get("/test",name="test")
async def read_users_me():
    url = router.url_path_for("login")
    return url