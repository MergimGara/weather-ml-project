import requests
import os
from dotenv import load_dotenv

# Lade Umgebungsvariablen
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city="Zurich", units="metric", lang="en"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,
        "lang": lang
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Fehler beim Abrufen der Wetterdaten: {response.status_code}, {response.text}")

# Testlauf (nur wenn direkt ausgeführt)
if __name__ == "__main__":
    weather_data = fetch_weather()
    print(weather_data)
