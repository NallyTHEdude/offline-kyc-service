from typing import Optional
from pydantic import BaseModel


class ErrorDetails(BaseModel):
    error: str
    description: str


class ApiError(BaseModel):
    success: bool = False
    status_code: Optional[int] = None
    message: str
    details: Optional[ErrorDetails] = None