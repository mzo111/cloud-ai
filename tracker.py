import json 
from weather import get_weather
from users import get_users
from datetime import datetime
class cityTracker:
    def __init__(self):
        self.data= []
    def build(self):
        print("fetching users....")
        users=get_users()
        for user in users:
            city = user['address']['city']
            print(f"Getting weather in {city}")
            temp=get_weather(city)
            entry ={
                "name": user['name'],
                "email":user['email'],
                "city":city,
                "temp":temp,
                
            }
            self.data.append(entry)
            print(f"\ndone {len(self.data)} users")
    def save(self):
        with open("tracker.json","w") as f:
            json.dump(self.data,f,indent=4)
        print ("saved to json file")
    def summary(self):
        if not self.data:
            print("No data")
            return
        for entry in self.data:
            temp = entry['temp']
            temp_display=f"{temp}" if temp is not None else "no temp"
            print(f"{entry['name']} | {entry['city']} | {temp_display}")
    def hottest(self):
        valid= [e for e in self.data if e ['temp'] is not None]
        if not valid:
            print("no temp")
            return
        hott= max(valid, key=lambda x: x['temp'])
        print(f"hottest city: {hott['city']} at {hott['temp']}")
    def test_with_real_cities(self):
        cities = ["Tucson", "London", "Dubai", "Tokyo", "Paris"]
        for city in cities:
            print(f"Getting weather in {city}...")
            temp = get_weather(city)
            entry = {
                "name": f"Test User ({city})",
                "email": f"test@{city.lower()}.com",
                "city": city,
                "temp": temp
            }
            self.data.append(entry)
tracker = cityTracker()
tracker.test_with_real_cities()
tracker.summary()
tracker.hottest()
tracker.save()