VALID_WEATHER = {"sunny", "rainy", "cloudy"} # Tillåtna vädertyper


def get_weather_choice():
    """Ask the user for a weather type and validate input.


Raises ValueError if the input is invalid.
"""
    weather = input("Enter weather type to filter (sunny/rainy/cloudy): ").strip().lower()  # Tar emot input från användaren
    
    if not weather:   # Om använderen inte anger nåt och trycker enter
        raise ValueError("Column name cannot be empty.")
    
    if weather not in VALID_WEATHER: # Om användaren anger icke tillåten input
        raise ValueError("Invalid weather type. Try: sunny, rainy, cloudy.")
    
    return weather