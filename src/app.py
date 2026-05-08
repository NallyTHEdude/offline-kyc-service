from fastapi import FastAPI
from src import healthCheckRouter
from src import ApiResponse

app = FastAPI()

# INCLUDE ROUTERS
api_prefix="/api"
app.include_router(healthCheckRouter, prefix=api_prefix)


# ROOT ENDPOINT
@app.get("/")
def read_root():
    response = ApiResponse(
        success=True,
        status_code=200,
        message="Welcome to the Offline KYC Service!"
    )
    return response.model_dump()