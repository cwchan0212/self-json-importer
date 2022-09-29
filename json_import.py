# Note: Import "randomuser" api json data via url or local file

## Step 1: Installation of packages
# Installation: MongoClient and requests
# pip install pymongo
# pip install requests

def main():
    
    import json, requests
    from pymongo import MongoClient

## Step 2: Fetch data
    
    # Option 1: Fetch json data from api url, e.g. request 10 results
    url = "https://randomuser.me/api/?results=10"
    response = requests.get(url)
    user = response.json()

# select the json objects
    user = user["results"]

    # Option 2: Fetch json data from local file
    # path = "C:/Temp/data10.json"
    # f = open(path, "r", encoding="utf-8")
    # user = json.load(f)["results"]

## Step 3: Connect of local MongoDB server

    # Create an instance of MongoClient. If the host localhost cannot be connected, please use 127.0.0.1.
    client = MongoClient("mongodb://localhost:27017/")
    
    # Select database.
    db = client["testdb"]
    
    # Select collection.
    duser = db["users"]

## Step 4: Import json data line by line

    # Insert each line of user objects, print **ObjectId** _id.
    for i in range(len(user)):
        u = user[i]
        # store and print the object id
        id = duser.insert_one(u).inserted_id
        print(id)

if __name__ == "__main__":
    main()