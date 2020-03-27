import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to mongoDB: %s") % e  


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_one({'first': 'martha'}, {'$set': {'gender': 'f'}})

documents = coll.find({'first': 'martha'})

for doc in documents:
    print(doc) 


# coll.remove({'first': 'douglas'})

# documents = coll.find({'first': 'douglas'})

# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_color': 'gray', 'nationality': 'english', 'occupation': 'writer'}

# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_color': 'not much', 'nationality': 'english', 'occupation': 'writer'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_color': 'white', 'nationality': 'american', 'occupation': 'writer'}]

# coll.insert_many(new_docs)