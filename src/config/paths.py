from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "data" / "weather_data.txt"
LOG_FILE = BASE_DIR / "logs.txt"