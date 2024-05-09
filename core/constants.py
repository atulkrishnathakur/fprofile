import os

from dotenv import load_dotenv
load_dotenv()

class Constants:
    ON: bool = True
    OFF: bool = False
    STATUS_UNAUTHORIZED=False
    STATUS_FORBIDDEN=False
    STATUS_OK=True

constants = Constants()