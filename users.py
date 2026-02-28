import requests
import json
def get_users():
    url= "https://jsonplaceholder.typicode.com/users"
    response=requests.get(url, timeout=10)
    users= response.json()
    print(f"total users fetched: {len(users)}")
    print("-"*20)
    for user in users:
        name= user['name']
        email=user['email']
        city = user['address']['city']
        company=user['company']['name']
        print(f"Name: {name}\n Email: {email}\n City: {city}\n Company: {company}")
        print("-"*40)
    with open("users.json", "w") as u:
        json.dump(users,u, indent=4)
    print("data saved")
   
def filter_by_city(city_name):
    with open("users.json","r") as f:
        users=json.load(f)
    matches=[user for user in users if user['address']['city'].lower()==city_name.lower()]
    if not matches:
        print(f"no users in {city_name}")
        return
    for user in matches:
        print(f"Name: {user['name']}| Email: {user['email']}")
get_users()  
city=input("enter a city to look for: ")
filter_by_city(city)


def load_users():
    with open("users.json", "r") as f:
        users=json.load(f)
    for user in users:
        print(f"name:{user['name']} | Email: {user['email']}")
load_users()