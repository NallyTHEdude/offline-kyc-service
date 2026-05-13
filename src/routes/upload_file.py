from fastapi import APIRouter, UploadFile, File, HTTPException
from src.core import *
from src.config import logger

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("upload file triggered_________")
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPG and PNG files are allowed.")

    with open(file.filename, "wb") as f:
        f.write(await file.read())
    
    qr_data = get_qr_data(file.filename)
    logger.info("QR Data extracted: %s", qr_data)
    image_data = get_image_data(file.filename)
    return qr_data