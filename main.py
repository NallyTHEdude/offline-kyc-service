import uvicorn
from src.config import env_config, logger

if __name__ == "__main__":
    logger.info(f"--------Starting server on {env_config.HOST}:{env_config.PORT}--------")
    uvicorn.run("src.app:app", host=env_config.HOST, port=env_config.PORT, reload=True)
