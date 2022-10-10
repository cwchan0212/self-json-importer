# Import "randomuser" JSON data from online source or local file
<a href="#"><img src="https://www.python.org/static/img/python-logo.png" width="100"></img></a>
<a href="#"><img src="https://webimages.mongodb.com/_com_assets/cms/kusb9stg1ndrp7j53-MongoDBLogoBrand1.png" width="100"></img></a>

MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays. 

The PyMongo distribution contains tools for interacting with MongoDB database from Python. The bson package is an implementation of the BSON format for Python. The pymongo package is a native Python driver for MongoDB. The gridfs package is a gridfs implementation on top of pymongo.

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

### Importing JSON file in MongoDB
In order to import a JSON in MongoDB, the user needs to first to load the JSON file and then insert that file into the database or collection. The steps are as follows:
1. Installation of MongoClient and Requests (for online source)
2. Fetch data from online source or local JSON file
3. Connect to the MongoDB Server on the (I) Local Machine or (II) MongoDB Atlas
4. Import JSON data line by line

## Step 1: Installation of MongoClient and Requests (for online source)
Installation: **MongoClient** and **Requests** 

```sh
pip install pymongo
pip install requests
```
If the user attempts to use **mongo+srv** protocol, **pymongo-srv** should be installed as follow:
```sh
pip install pymongo[srv]  # for connecting to MongoDB Atlas
```

## Step 2: Fetch data from online source or local JSON file
Option 1: Fetch JSON data from api url. let use randomuser.me as an example, e.g. request 100 results
```sh
url = "https://randomuser.me/api/?results=100"
response = requests.get(url)
user = response.json()
```
Select the json objects 
```sh
user = user["results"] 
```
Option 2: Fetch JSON data from local file
```sh
path = "C:/Temp/data10.json"
f = open(path, "r", encoding="utf-8")
user = json.load(f)["results"]
```
## Step 3: Connect to the MongoDB Server on the Local Machine or MongoDB Atlas
Create an instance of MongoClient to connect to the MongoDB Server on the **Local Machine**. If the host "**localhost**" cannot be connected, please use "**127.0.0.1**".

```sh
url = "mongodb://localhost:27017/"
```
Create an instance of MongoClient to connect **MongoDB Atlas**.
```sh
url = "mongodb+srv://<username>:<password>@<mongoserver>/testdb?retryWrites=true&w=majority"
```

Connect to the MongoDB server with the try-catch command.
```
client = MongoClient(url)
try:
    print(client.server_info())                 # Print server info
except Exception:
    print("Unable to connect to the server.")   # Print error message to the server
```

Select database.
```sh
db = client["testdb"]
```

select collection.
```sh
duser = db["users"]
```
## Step 4: Import JSON data line by line
Insert each line of user objects, print **ObjectId** _id.
```sh
for i in range(len(user)):
    u = user[i]
    id = duser.insert_one(u).inserted_id
    print(id)
```

## Compplete Code

I. Connect to the MongoDB Server on the Local Machine (json-import_local.py)

```sh
def main():

    import json, requests
    from pymongo import MongoClient

    url = "https://randomuser.me/api/?results=100"
    response = requests.get(url)
    user = response.json()
    user = user["results"]

    ## Fetch json data from local file
    # path = "C:/Temp/data10.json"
    # f = open(path, "r", encoding="utf-8")
    # user = json.load(f)["results"]
    
    # Create an instance of MongoClient. If the host localhost cannot be connected, please use 127.0.0.1.
    url = "mongodb://localhost:27017/"
    client = MongoClient(url)
    
    try:
        print(client.server_info())
        db = client["testdb"]
        duser = db["users"]
        for i in range(len(user)):
            u = user[i]
            # store and print the object id
            id = duser.insert_one(u).inserted_id
            print(id)
    except Exception:
        print("Unable to connect to the server.")
        
if __name__ == "__main__":
    main()
```

II. Connect to MongoDB Atlas (json-import_remote.py)
```sh
def main():

    import json, requests
    from pymongo import MongoClient
    ## Connect to MongoDB Atlas
    from pymongo.server_api import ServerApi
    from pymongo.mongo_client import MongoClient
    
    url = "https://randomuser.me/api/?results=100"
    response = requests.get(url)
    user = response.json()
    user = user["results"]

    ## Fetch json data from local file
    # path = "C:/Temp/data10.json"
    # f = open(path, "r", encoding="utf-8")
    # user = json.load(f)["results"]
    
    # Create an instance of MongoClient to connect to MongoDB Atlas.
    url = "mongodb+srv://<username>:<password>@<mongoserver>/testdb?retryWrites=true&w=majority"

    client = MongoClient(url)
    
    try:
        print(client.server_info())
        db = client["testdb"]
        duser = db["users"]
        for i in range(len(user)):
            u = user[i]
            # store and print the object id
            id = duser.insert_one(u).inserted_id
            print(id)
    except Exception:
        print("Unable to connect to the server.")
        
if __name__ == "__main__":
    main()
```

## Command
```sh
# Connect to the MongoDB Server on the Local Machine
python json-import_local.py
# Connect to MongoDB Atlas
python json-import_remote.py
```