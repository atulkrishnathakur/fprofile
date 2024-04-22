import os

from dotenv import load_dotenv
from typing import Dict
load_dotenv()

class Settings:
    PROJECT_NAME: str = "fprofile"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM =  os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    TOKEN_TYPE: str = "bearer"
    AUTH_HEADER: Dict[str,str] = {"WWW-Authenticate": "Bearer"}

settings = Settings()