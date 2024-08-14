from pydantic import BaseModel, model_validator, EmailStr
from typing import List

class BaseUserSchema(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr
    username:str | None = None
    role: int
    country: int
    state: int
    city: int
    address: str| None = None
    zeep_code:str | None = None

class BaseUserListSchema(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    email: EmailStr

class UserSchemaIn(BaseUserSchema):
    password: str
    confirm_password:str

    @model_validator(mode='after')
    def check_passwords_match(self):
        pw1 = self.password
        pw2 = self.confirm_password
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self

class UserSchemaOut(BaseUserSchema):
    status_code:int | None = None
    status:bool | None = None

class UserInDB(BaseUserSchema):
    hashed_password: str


class AllUserSchemaOut(BaseModel):
    status_code:int | None = None
    status:bool | None = None
    data: list[BaseUserListSchema] | None = None

class ImageData(BaseModel):
    image_base64: str | None = None

class Test(BaseModel):
    username: str | None = None
    email: str | None = None
    full_name: str | None = None