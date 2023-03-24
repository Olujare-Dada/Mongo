from pymongo import MongoClient


try:
    conn = MongoClient('mongodb://127.0.0.1:27017/pythonDatabase')
    print("Connected successfully!")
except:
    print("Could not connect to MongoDB")


db = conn.get_database()

collection_name = db["firstPyTable"]


item_1 = {

    "item_name":"Blender",
    "max_discount":"10%",
    "batch_number":"RR450020FRG",
    "price":340,
    "category":"kitchen appliance"

    }

collection_name.insert_one(item_1)
