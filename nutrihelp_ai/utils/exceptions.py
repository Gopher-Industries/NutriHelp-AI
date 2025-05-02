from fastapi import HTTPException, status
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE

class ModelNotLoadedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The prediction model is not currently available."
        )

class InvalidInputException(HTTPException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

class ModelNotLoadedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=HTTP_503_SERVICE_UNAVAILABLE, detail="Model or preprocessor not loaded.")