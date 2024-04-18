from database.model.user import User
from core.hashing import HashData

def create_new_user(db, user):
    db_user = User(first_name=user.first_name,last_name=user.last_name,username=user.username,email=user.email,hashed_password=HashData.create_password_hash(user.password),country=user.country,state=user.state,city=user.city,role=user.role,zeep_code=user.zeep_code,address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
