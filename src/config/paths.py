from pathlib import Path


# BASE_DIR points to the project root (three parents up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "data" / "weather-data.txt"
LOG_FILE = BASE_DIR / "logs.txt"