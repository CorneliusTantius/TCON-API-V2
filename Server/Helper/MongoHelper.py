import os
from json import load
from pymongo import MongoClient

def GetMongoClient(collection_name):
    connection_string = ""
    try:
        print("> trying to load config from json")
        config = load( open("Server/configuration.json") )
        connection_string = config["DatabaseUrl"]
    except:
        print("> loading config from os variable")
        try:
            connection_string = os.environ["DatabaseUrl"]
        except:
            print("> failed to load from environment variable")
    client = MongoClient(connection_string)["master"]
    return client[collection_name]