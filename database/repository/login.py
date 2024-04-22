from database.model.user import User
from sqlalchemy.orm import Session
from schema.user import UserInDB

def get_user(db, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user
