from fastapi import APIRouter, UploadFile, File, HTTPException
from src.core import *
from src.schemas import ApiResponse
from src.config import TEMP_DIR, logger
from uuid import uuid4


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = None
    try:
        logger.info("Received file upload request: {}, content type: {}", file.filename, file.content_type)

        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPG and PNG files are allowed.")
        unique_filename = f"{uuid4().hex}_{file.filename}"
        file_path = TEMP_DIR / unique_filename

        with open(file_path, "wb") as f:
            f.write(await file.read())

        verification_status = compare_qr_data_with_image_data(str(file_path))

        return ApiResponse(
            success=True,
            status_code=200,
            message=(
                "Adhaar Verified Successfully"
                if verification_status["verified"]
                else "Adhaar verification failed"
            ),
            data={
                "name_match": verification_status["name_match"],
                "dob_match": verification_status["dob_match"],
                "gender_match": verification_status["gender_match"],
                "verified": verification_status["verified"],
            }
        )

    except Exception as e:
        logger.error("Error processing file upload: {}", str(e))

        raise HTTPException(status_code=500, detail="Failed to process uploaded file.")

    finally:
        if file_path and file_path.exists():
            file_path.unlink()