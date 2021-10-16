import os
from json import load
from pymongo import MongoClient
from .Logger import Logger

def GetMongoClient(collection_name):
    connection_string = ""
    try:
        Logger.LogInformation("trying to load config from json")
        config = load( open("Server/configuration.json") )
        connection_string = config["DatabaseUrl"]
    except:
        Logger.LogInformation("loading config from os variable")
        try:
            connection_string = os.environ["DatabaseUrl"]
        except:
            Logger.LogError("failed to load from environment variable")
            return None
    client = MongoClient(connection_string)["master"]
    return client[collection_name]