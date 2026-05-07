from typing import Optional, Any
from pydantic import BaseModel

class ApiResponse(BaseModel):
    success: bool = True
    status_code: int
    message: str
    data: Optional[Any] = None