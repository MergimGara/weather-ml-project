from src.fetch_weather import get_weather_data
from src.db_connector import init_supabase
from datetime import datetime

def ingest_weather_data(city: str):
    # 1. Wetterdaten holen
    weather = get_weather_data(city)
    
    if weather is None:
        print("❌ Fehler beim Abrufen der Wetterdaten.")
        return

    # 2. Supabase verbinden
    supabase = init_supabase()

    # 3. Daten vorbereiten für Insert
    data = {
        "city": city,
        "timestamp": datetime.utcnow().isoformat(),  # UTC-Zeit
        "temperature_c": weather["temperature"],
        "humidity_percent": weather["humidity"],
        "weather_condition": weather["condition"]
    }

    # 4. Insert
    response = supabase.table("weather_data").insert(data).execute()

    if response.data:
        print(f"✅ Wetterdaten für {city} erfolgreich gespeichert.")
    else:
        print(f"❌ Fehler beim Speichern: {response.error}")

# Manuell testen
if __name__ == "__main__":
    ingest_weather_data("Zurich")
