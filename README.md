## JSON Importer

### Introduction
Developed a tool using Python script that allows for easy import of JSON data from online sources to MongoDB Atlas.
Utilized Python, MongoDB, and JSON to build the application.

#### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites
To use this tool, you will need:

* Python 3
* Pymongo
* Requests 

To install the required packages, you can use pip:
```
pip install pymongo
pip install requests
```
> Note: 
If the user attempts to use **mongo+srv** protocol, **pymongo-srv** should be installed as follow:
```sh
pip install pymongo[srv]  # for connecting to MongoDB Atlas
```

### Usage

In order to import a JSON in MongoDB, the user needs to first to load the JSON file and then insert that file into the database or collection. The steps are as follows:
1. Installation of MongoClient and Requests (for online source)
2. Fetch data from an online source or local JSON file
3. Connect to the MongoDB Server on the (I) Local Machine or (II) MongoDB Atlas
4. Import JSON data line by line

#### Step 1: Installation of MongoClient and Requests (for online source)
Installation: **MongoClient** and **Requests** 

```sh
pip install pymongo
pip install requests
```
If the user attempts to use **mongo+srv** protocol, **pymongo-srv** should be installed as follow:
```sh
pip install pymongo[srv]  # for connecting to MongoDB Atlas
```

#### Step 2: Fetch data from online source or local JSON file
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
#### Step 3: Connect to the MongoDB Server on the Local Machine or MongoDB Atlas
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
#### Step 4: Import JSON data line by line
Insert each line of user objects, print **ObjectId** _id.
```sh
for i in range(len(user)):
    u = user[i]
    id = duser.insert_one(u).inserted_id
    print(id)
```
##### Command
##### Connect to the MongoDB Server on the Local Machine
```
python json-import_local.py
# Connect to MongoDB Atlas
python json-import_remote.py
```
