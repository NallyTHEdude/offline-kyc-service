import sys
from loguru import logger
from src.config import env_config
from pathlib import Path

logger.remove()

if env_config.ENV == "dev":
    logger.level("INFO", color="<green>")
    logger.level("WARNING", color="<yellow>")
    logger.level("ERROR", color="<red>")
    logger.level("DEBUG", color="<blue>")
    logger.level("CRITICAL", color="<RED>")

    logger.add(
        sys.stdout,
        level="DEBUG",
        colorize=True,
        backtrace=True,
        diagnose=True,
        format=(
            "{time:YYYY-MM-DD HH:mm:ss} | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{line}</cyan> | "
            "<level>{message}</level>"
        )
    )

else:
    Path("logs").mkdir(exist_ok=True)
    logger.add(
        "logs/app.logs",
        level="INFO",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        enqueue=True,
        format=(
            "{{"
            "\"time\": \"{time:YYYY-MM-DD HH:mm:ss}\", "
            "\"level\": \"{level}\", "
            "\"message\": \"{message}\""
            "}}"
        )
    )