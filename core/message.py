import os

from dotenv import load_dotenv
load_dotenv()

class Message:
    INCORRECT_CREDENTIALS: str = "Incorrect username or password"
    LOGOT_SUCCESS: str = "Logout Successfull"
    NEED_TO_LOGIN: str = "You have need to login first"
    INACTIVE_USER: str = "Inactive User"

message = Message()
