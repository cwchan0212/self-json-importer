# Note to import json data from api url or local file

# Part 1: Installation of packages
# Installation: MongoClient & requests# 
# pop install pymongo
# pip install requests

import json, requests
from pymongo import MongoClient

# Part 2: Fetch data
# - 1: fetch json data from api url
# installation pip install requests
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
user = response.json()

# select the json objects
user = user["results"]

# - 2: fetch json data from local file
# path = "C:/Temp/data10.json"
# f = open(path, "r", encoding="utf-8")
# user = json.load(f)["results"]

# Part 3: Connect of local MongoDB server
# create an instance of MongoClient
client = MongoClient("mongodb://localhost:27017/")
# select database
db = client["testdb"]
# select collection
duser = db["users"]

# insert each line of user objects
for i in range(len(user)):
    u = user[i]
    # store and print the object id
    id = duser.insert_one(u).inserted_id
    print(id)