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

router = APIRouter()

@router.post("/save-user",response_model=UserSchemaOut,response_class=JSONResponse,name="saveuser")
def save_user(user: UserSchemaIn, db:Session = Depends(get_db)):
    try:
        inserted_user = create_new_user(db=db, user=user)
        http_status_code = status.HTTP_200_OK
        user_data = {
            "status_code": http_status_code,
            "status":True,
            "first_name": inserted_user.first_name,
            "email": inserted_user.email,
            "role": inserted_user.role,
            "country":inserted_user.country,
            "state":inserted_user.state,
            "city":inserted_user.city
        }
        response_data = UserSchemaOut(**user_data)
        response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
    except ValueError as e:
        http_status_code = 500
        error_detail = f"Invalid response data: {e}"
        response_data = {
            "status_code": http_status_code,
            "status": False,
            "detail": error_detail
        }
        response = JSONResponse(content=response_data, status_code=http_status_code)
    return response


@router.post("/user-list",response_model=AllUserSchemaOut,name="userlist")
def userlist(current_user: Annotated[UserSchemaOut, Depends(get_current_active_user)],db:Session = Depends(get_db)):
    try:
        allUser = get_all_user(db)

        http_status_code = status.HTTP_200_OK
        ulist = list()

        for u in allUser:
            mydict = {}
            mydict['id'] = u.id
            mydict['first_name'] = u.first_name
            mydict['last_name'] = u.last_name
            mydict['email'] = u.email
            ulist.append(mydict)
            
        user_data = {
            "status_code": http_status_code,
            "status":True,
            "data":ulist
        }
        response_data = AllUserSchemaOut(**user_data)
        response = JSONResponse(content=response_data.dict(),status_code=http_status_code)

    except ValueError as e:
        http_status_code = 500
        user_data = {
            "status_code": http_status_code,
            "status":False,
        }
        response = JSONResponse(content=user_data,status_code=http_status_code)
    return response

@router.post('/upload-image',name="uploadimage")
def upload_image(current_user: Annotated[UserSchemaOut, Depends(get_current_active_user)],db:Session = Depends(get_db), image_data:ImageData = None ):
    try:
        # decode the base64
        image_data_bytes = base64.b64decode(image_data.image_base64)
        N = 7
        randstr = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
        # Define the path to save the image
        uploaddir = "uploads"
        filename="profile_"+randstr+".png"
        file_path = os.path.join(uploaddir,filename)

        #save the image
        with open(file_path, "wb") as image_file:
            image_file.write(image_data_bytes)
        

        updateduser = update_user(db=db, currentUser=current_user, profileImage=filename)
        mydict = {}
        mydict['photimage'] = f"/"+file_path

        http_status_code = status.HTTP_200_OK
        uploaded_data = {
            "status_code": http_status_code,
            "status":True,
            "data":mydict
        }
        response = JSONResponse(content=uploaded_data,status_code=http_status_code)
        return response
    except ValueError as e:
        http_status_code = 500
        data = {
            "status_code": http_status_code,
            "status":False,
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response


@router.post("/upload-image-pillow", name="uploadimage_pillow")
def upload_image_pillow(current_user: Annotated[UserSchemaOut, Depends(get_current_active_user)],db:Session = Depends(get_db), image_data:ImageData = None):
    try:
        # Decode the base64 image
        image_data_bytes = base64.b64decode(image_data.image_base64)
        N = 7
        randstr = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
        uploaddir = "uploads"
        filename="profile_pillow_"+randstr+".png"
        file_path = os.path.join(uploaddir,filename)

        # Convert binary data to an image
        image = Image.open(io.BytesIO(image_data_bytes))

        # Save the image to a dictionary
        image.save(uploaddir+'/'+filename)
        updateduser = update_user(db=db, currentUser=current_user, profileImage=filename)
        mydict = {}
        mydict['photimage'] = f"/"+file_path
        http_status_code = status.HTTP_200_OK
        uploaded_data = {
            "status_code": http_status_code,
            "status":True,
            "data":mydict
        }
        response = JSONResponse(content=uploaded_data,status_code=http_status_code)
        return response

    except ValueError as e:
        http_status_code = 500
        data = {
            "status_code": http_status_code,
            "status":False,
            }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response