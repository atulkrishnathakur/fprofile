from fastapi.security import APIKeyHeader
from fastapi import Security
from core.config import settings
from passlib.context import CryptContext
from core.logger import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

header_scheme = APIKeyHeader(name=settings.API_KEY_HEADER_NAME)

async def get_api_key(api_key: str = Security(header_scheme)):
    logger.debug(api_key)
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your custom message here",
            headers={"WWW-Authenticate": ""},
        )
    return api_key
