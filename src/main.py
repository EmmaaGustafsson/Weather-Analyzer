"""Main entry point for WeatherHelper.


Run this file from the project root with:


python src/main.py


The script adjusts sys.path so that imports for the packages under `src/` work
when running the file directly.
"""


from pathlib import Path
import sys


# Ensure `src` directory is on sys.path so `weather`, `config`, etc. import correctly
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))


from weather.weather_analyzer import WeatherAnalyzer
from config.paths import DATA_FILE
from logger.custom_logger import get_logger
from utils.input_handler import get_weather_choice




def main():
    logger = get_logger("WeatherAnalyzer")

    try:
        logger.info("Program started.")

        analyzer = WeatherAnalyzer(DATA_FILE)
        analyzer.load_data()

        print(f"Total days in file: {analyzer.number_of_days()}")

        highest = analyzer.highest_temperature()
        if highest is None:
            print("No data available.")
        else:
            print(f"Highest temperature: {highest[1]}°C on {highest[0]}")

        try:
            weather_choice = get_weather_choice()
        except ValueError as e:
            print(f"Invalid input: {e}")
            logger.error(f"Input error: {e}")
            return

        filtered = analyzer.filter_by_weather(weather_choice)

        print(f"\nDays with '{weather_choice}':")
        if not filtered:
            print("(none)")
        else:
            for day, temp, weather in filtered:
                print(f"{day}: {temp}°C")

        logger.info("Program finished successfully.")

    except Exception as e:
        logger.error(f"Error: {e}")
        print("An error occurred. Check logs.txt for details.")


if __name__ == "__main__":
    main()
