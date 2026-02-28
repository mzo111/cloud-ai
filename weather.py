import requests

def get_weather(city):
    try:
    # Step 1: convert city name to coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url, timeout=10)
        geo_data = geo_response.json()
        if not geo_data.get('results'):
            print (f"City {city} does not exist or is not supported")
            return None
        lat = geo_data['results'][0]['latitude']
        lon = geo_data['results'][0]['longitude']
        
        # Step 2: get weather using coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url, timeout=10)
        weather_data = weather_response.json()
        
        temp = weather_data['current_weather']['temperature']
        return temp
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")
        return None
    except Exception as e:
        print(f"error occured: {e}")
        return None
