from fastapi import FastAPI
from src.routes import *
from src.utils import ApiResponse

app = FastAPI()

# INCLUDE ROUTERS
api_prefix="/api"
app.include_router(healthCheckRouter, prefix=api_prefix)
app.include_router(uploadFileRouter, prefix=api_prefix)


# ROOT ENDPOINT
@app.get("/")
def read_root():
    response = ApiResponse(
        success=True,
        status_code=200,
        message="Welcome to the Offline KYC Service!"
    )
    return response.model_dump()