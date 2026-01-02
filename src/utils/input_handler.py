VALID_WEATHER = {"sunny", "rainy", "cloudy"}


"""Ask the user for a weather type and validate input.


Raises ValueError if the input is invalid.
"""

def get_weather_choice():
    weather = input("Enter weather type to filter (sunny/rainy/cloudy): ").strip().lower()
    
    if not weather:
        raise ValueError("Column name cannot be empty.")
    
    if weather not in VALID_WEATHER:
        raise ValueError("Invalid weather type. Try: sunny, rainy, cloudy.")
    
    return weather