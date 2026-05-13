from fastapi import APIRouter 
from src.utils import ApiResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return ApiResponse(
        success=True,
        status_code=200,
        message="Service is healthy"
    )