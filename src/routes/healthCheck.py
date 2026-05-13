from fastapi import APIRouter 
from src.schemas import ApiResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return ApiResponse(
        success=True,
        status_code=200,
        message="Service is healthy"
    )