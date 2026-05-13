from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
TEMP_DIR = ROOT_DIR / "_temp"

TEMP_DIR.mkdir(exist_ok=True)