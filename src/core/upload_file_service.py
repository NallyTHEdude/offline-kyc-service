import cv2
import gzip
from pyzbar.pyzbar import decode
from src.config import logger
from src.schemas import ApiResponse, ApiError, AdhaarData
import re


# ----------Important Helper Functions -----------
def get_qr_data(image_path):
    try:
        preprocessed = _preprocess_image(image_path)
        decoded_data = detect_and_decode_qr(preprocessed)
        if decoded_data:
            extracted = _extract_data(decoded_data)
            adhaar_data = AdhaarData(
                name=extracted.get("name", None),
                date_of_birth=extracted.get("dob", None),
                gender=extracted.get("gender", None),
                phone_no=extracted.get("phone_no", None)
            )
            return ApiResponse(
                success=True,
                status_code=200,
                message="QR code data extracted successfully.",
                data=adhaar_data
            )
        else:
            raise ValueError("No QR code detected in the image.")
    except Exception as e:
        logger.error("Error in get_qr_data: {}", str(e))
        return ApiError(
            success=False,
            status_code=400,
            message="Failed to extract QR code data.",
            details= ApiError.ErrorDetails(
                error="QRExtractionError",
                description="Could Not Extract QR data from the image. Error: {}".format(str(e))
            )
        )

# TODO: IMPLEMEMT OCR to extract text data from image if QR code is not detected
def get_image_data(image_path):
    pass

# ---------- Helper Functions -----------
def _preprocess_image(image_path):
    logger.info("Reading image from path: {}", image_path)
    image = cv2.imread(image_path)
    if image is None:
        logger.error("Could not read image at path: {}", image_path)
        raise ValueError("Invalid image path.")
    logger.info("Image read successfully.")
    processed = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    return processed

def detect_and_decode_qr(image):
    logger.info("Detecting QR code in the image.")
    decoded_objects = decode(image)
    if not decoded_objects:
        logger.error("QR not detected during detect_and_decode_qr")
        return None
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        return data

def _extract_data(decoded_qr_str):
    num = int(decoded_qr_str)
    byte_data = num.to_bytes((num.bit_length() + 7) // 8,'big')
    decompressed = gzip.decompress(byte_data)
    data_parts = decompressed.split(b'\xff')
    logger.info("Data parts count: {}", len(data_parts))
    decoded_parts = []
    for part in data_parts:
        try:
            decoded_parts.append(part.decode("utf-8"))
        except Exception:
            decoded_parts.append("")
    phone_no = None
    for value in decoded_parts:
        if re.fullmatch(r"XXXXXX\d{4}", value):
            phone_no = value
            break
    data ={
        "name": decoded_parts[3],
        "dob": decoded_parts[4],
        "gender": decoded_parts[5],
        "phone_no": phone_no
    }

    return data