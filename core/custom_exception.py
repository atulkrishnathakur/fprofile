class CustomException(Exception):
    def __init__(self, status_code: int, status:bool | None=None, message:str | None=None, data:list | None=None):
        self.status_code = status_code
        self.status = status
        self.message = message
        self.data = data
