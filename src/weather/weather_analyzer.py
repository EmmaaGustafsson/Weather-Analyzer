class WeatherAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath  # Sökvägen till texfilen med väderdata
        self.data = []            # Gör datan till en lista med tuplar

    def load_data(self):
        with open(self.filepath, "r", encoding="utf-8") as f:   # Öppnar filen på ett säkert sätt
            for line in f:
                parts = line.strip().split()   # Tar bort radbrytning och och delar upp raderna i delar
                if len(parts) != 3:            # Hoppa över om raden inte har 3 delar
                    continue
                day, temp_str, weather = parts
                try:                           # Försöker göra temperaturen till heltal, hoppa över raden om det inte går
                    temp = int(temp_str)
                except ValueError:
                    continue
                self.data.append((day, temp, weather)) # Lägger till datan i listan
        return self.data

    def number_of_days(self):    # Returnerar antalet dagar (rader) som finns i datan
        return len(self.data)

    def highest_temperature(self):   # Om ingen data existerar returnera inget
        if not self.data:
            return None
        return max(self.data, key=lambda x: x[1])  # Hittar posten (raden) med högst temperatur (index 1 i listan)

    def filter_by_weather(self, weather_type):     # Returnerar en lista med alla poster som matchar angedd vädertyp
        return [entry for entry in self.data if entry[2].lower() == weather_type.lower()]
