from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class _EnvConfig(BaseModel):
    ENV: str = os.getenv("ENV")
    PORT: int = int(os.getenv("PORT")) 
    HOST: str = os.getenv("HOST")

env_config = _EnvConfig()