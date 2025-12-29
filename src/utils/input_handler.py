VALID_WEATHER = {"sunny", "rainy", "cloudy"}




def get_weather_choice():
"""Ask the user for a weather type and validate input.


Raises ValueError if the input is invalid.
"""
weather = input("Enter weather type to filter (sunny/rainy/cloudy): ").strip().lower()


if not weather:
raise ValueError("Column name cannot be empty.")


if weather not in VALID_WEATHER:
raise ValueError("Invalid weather type. Try: sunny, rainy, cloudy.")


return weather