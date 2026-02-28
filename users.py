import requests
import json
def get_users():
    url= "https://jsonplaceholder.typicode.com/users"
    response=requests.get(url, timeout=10)
    users= response.json()
    with open("users.json", "w") as u:
        json.dump(users,u, indent=4)
    return users

   
def filter_by_city(city_name):
    with open("users.json","r") as f:
        users=json.load(f)
    matches=[user for user in users if user['address']['city'].lower()==city_name.lower()]
    return matches

def load_users():
    with open("users.json", "r") as f:
        users=json.load(f)
    return users
