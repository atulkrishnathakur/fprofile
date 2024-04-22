import os

from dotenv import load_dotenv
load_dotenv()

class Message:
    INCORRECT_CREDENTIALS: str = "Incorrect username or password"

message = Message()