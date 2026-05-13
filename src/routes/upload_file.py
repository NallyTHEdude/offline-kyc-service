from fastapi import APIRouter, UploadFile, File, HTTPException
from src.core import *
from src.schemas import ApiResponse
from src.config import logger

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("upload file triggered_________")
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPG and PNG files are allowed.")

    with open(file.filename, "wb") as f:
        f.write(await file.read())
    
    verification_status = compare_qr_data_with_image_data(file.filename)
    return ApiResponse(
        success=True,
        status_code=200,
        message="Adhaar Verified Successfully" if verification_status["verified"] else "Adhaar verification failed",
        data = {
            "name_match": verification_status["name_match"],
            "dob_match": verification_status["dob_match"],
            "gender_match": verification_status["gender_match"],
            "verified": verification_status["verified"],
        }

    )