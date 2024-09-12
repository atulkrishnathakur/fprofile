from fastapi import APIRouter
from fastapi import Depends
from fastapi import status, BackgroundTasks
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
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig,MessageType
from schema.email import EmailSchema
from core.fastapi_mail_config import mailconf

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

@router.post("/sendmail-fastapi-mail",name="sendmail_fastapi_mail")
async def sendmail_with_fastapi_mail(email: EmailSchema,current_user: Annotated[UserSchemaOut, Depends(get_current_active_user)],db:Session = Depends(get_db)):
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(mailconf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

@router.post("/sendmail-fastapi-mail-background",name="sendmail_fastapi_mail_background")
async def sendmail_with_fastapi_mail(background_tasks: BackgroundTasks,email: EmailSchema,current_user: Annotated[UserSchemaOut, Depends(get_current_active_user)],db:Session = Depends(get_db)):
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(mailconf)
    background_tasks.add_task(fm.send_message,message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})