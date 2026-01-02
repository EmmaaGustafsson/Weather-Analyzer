class WeatherAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def load_data(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue
                day, temp_str, weather = parts
                try:
                    temp = int(temp_str)
                except ValueError:
                    continue
                self.data.append((day, temp, weather))
        return self.data

    def number_of_days(self):
        return len(self.data)

    def highest_temperature(self):
        if not self.data:
            return None
        return max(self.data, key=lambda x: x[1])

    def filter_by_weather(self, weather_type):
        return [entry for entry in self.data if entry[2].lower() == weather_type.lower()]
