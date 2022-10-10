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