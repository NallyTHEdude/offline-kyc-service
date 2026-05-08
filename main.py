import uvicorn
from src.config import env_config

if __name__ == "__main__":
    uvicorn.run("src.app:app", host=env_config.HOST, port=env_config.PORT, reload=True)
