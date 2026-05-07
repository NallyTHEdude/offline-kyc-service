from fastapi import APIRouter 
import src.app as app

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "200", "message": "Service is healthy"}