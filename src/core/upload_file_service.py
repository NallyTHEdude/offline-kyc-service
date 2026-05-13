import cv2
import gzip
from pyzbar.pyzbar import decode
from src.config import logger


def get_qr_data(image_path):
    try:
        preprocessed = _preprocess_image(image_path)
        decoded_data = detect_and_decode_qr(preprocessed)
        if decoded_data:
            extracted = _extract_data(decoded_data)
            return extracted
        else:
            raise ValueError("No QR code detected in the image.")
    except Exception as e:
        logger.error("Error in get_qr_data: %s", str(e))
        return None
    
# TODO: IMPLEMEMT OCR to extract text data from image if QR code is not detected
def get_image_data(image_path):
    pass

# ---------- Helper Functions -----------
def _preprocess_image(image_path):
    logger.info("Reading image from path: %s", image_path)
    image = cv2.imread(image_path)
    if image is None:
        logger.error("Could not read image at path: %s", image_path)
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
        logger.info("Decoded: %s", data)
        return data


#TODO: handle data properly instead of hardcoding indices
def _extract_data(decoded_qr_str):
    num = int(decoded_qr_str)
    byte_data = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    decompressed = gzip.decompress(byte_data)

    name, dob, gender, phone_no = None, None, None, None

    data_parts = decompressed.split(b'\xff')
    for i, part in enumerate(data_parts):
        if i==3:
            name = part.decode('utf-8')
        elif i==4:
            dob = part.decode('utf-8')
        elif i==5:
            gender = part.decode('utf-8')
        elif i==17:
            phone_no = part.decode('utf-8')
    return {
        "name": name,
        "dob": dob,
        "gender": gender,
        "phone_no": phone_no
    }