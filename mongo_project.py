import pymongo
import os
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to mongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option")
    return option


def add_record():
    print("")
    first = input("Enter first name >")
    last = input("Enter Last name >")
    dob = input("Enter date of birth >")
    gender = input("Enter gender >")
    hair_color = input("Enter hair color >")
    occupation = input("Enter occupation >")
    nationality = input("Enter nationality >")


new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob,'gender': gender, 'hair_color': hair_color, 'occupation': occupation, 'nationality': nationality}

try:
    coll.insert_one(new_doc)
    print("")
    print("Document inserted")
except:
    print("Error accessing database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


main_loop()
