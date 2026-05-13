from pydantic import BaseModel

class AdhaarData(BaseModel):
    name: str
    date_of_birth: str
    gender: str
    phone_no: str
