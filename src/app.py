from fastapi import FastAPI


app = FastAPI()

# IMPORT ROUTERS
from src.routes.healthCheck import router as healthCheck

# INCLUDE ROUTERS
api_prefix="/api"
app.include_router(healthCheck, prefix=api_prefix)


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"message": "Welcome to the Offline KYC Service!"}