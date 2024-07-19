from fastapi.security import APIKeyHeader
from core.config import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

header_scheme = APIKeyHeader(name=settings.API_KEY_HEADER_NAME)
