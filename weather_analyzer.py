
class WeatherAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def load_data(self):
        while open(self.filepath, "r", encoding = "utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue