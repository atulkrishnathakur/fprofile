from typing import Annotated
from fastapi import Depends, status
from jose import jwt
from sqlalchemy.orm import Session
from database.session import get_db
from core.hashing import HashData
from core.config import settings
from core.security import create_access_token, blacklist
from core.message import message
from core.constants import constants
#from core.custom_exception import CustomException
from database.repository.login import get_user
from schema.token import Token, TokenData, TokenCredentialIn,TokenOut, Logout
from schema.user import UserSchemaOut
from core.apikeyheader import header_scheme, get_api_key
from core.logger import logger
from fastapi import HTTPException, Response, Request


def authenticate_user(username,password,db):
    logger.debug('authenticate user function')
    user = get_user(db,username)
    if not user:
        return False
    if not HashData.verify_password(password, user.hashed_password):
        return False    
    return user
'''

def authenticate_user(username,password,db):
    pass
 

'''
async def get_current_user(token: Annotated[str, Depends(get_api_key)], db: Annotated[Session, Depends(get_db)]):
    logger.debug('get current user function')
    if token in blacklist:
        http_status_code = status.HTTP_401_UNAUTHORIZED 
        #raise CustomException(status_code=http_status_code,status=constants.STATUS_UNAUTHORIZED,message=message.NEED_TO_LOGIN,data=[])
    else:    
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("email")
        token_data = TokenData(email=email)
        user = get_user(db, email=token_data.email)
        return user

'''

async def get_current_user(token: Annotated[str, Depends(get_api_key)], db: Annotated[Session, Depends(get_db)]):
    pass 

'''
async def get_current_active_user(
    current_user: Annotated[UserSchemaOut, Depends(get_current_user)],
):
    logger.debug('get active user function')
    if(current_user.is_active == False):
        #raise CustomException(status_code=status.HTTP_403_FORBIDDEN,status=constants.STATUS_FORBIDDEN,message=message.INACTIVE_USER,data=[])    
        pass
    return current_user

'''

async def get_current_active_user(
    current_user: Annotated[UserSchemaOut, Depends(get_current_user)],
):
    pass
'''    