from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from typing import Annotated
from sqlalchemy.orm import Session
from schema.user import UserSchemaOut, UserSchemaIn, BaseUserSchema, AllUserSchemaOut, ImageData
from database.session import get_db
from database.repository.user import create_new_user, get_all_user,update_user
from fastapi.responses import JSONResponse, ORJSONResponse
from database.repository.login import get_user
from core.auth import authenticate_user, get_current_active_user
import base64
import os
import io
from PIL import Image
import string
import random
from smtplib import SMTP

router = APIRouter()

@router.get("/sendmail-smtplib",name="sendmail_smtplib")
def sendmail_with_smtplib(db:Session = Depends(get_db)):
    # list of email_id to send the mail
    eli = ["akt9@gmail.com", "testy@yopmail.com"]
    for dest in eli:
        # creates SMTP session
        s = SMTP('smtp.gmail.com', 587)
        # start tls fo security
        s.starttls()
        # Authentication
        s.login("softtestinfo@gmail.com", "kmbonzewdsmorthm")
        # message to be sent
        message = "Hi, This is my simple python mail"
        # sending the mail
        s.sendmail("atul77.cs@gmail.com", dest, message)
        # terminating the session
        s.quit()
    return "mail sent"