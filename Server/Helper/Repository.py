### Package Import ###
from typing import List
from bson import ObjectId
from pydantic import parse, parse_obj_as
### AppCode Import ###
from Server.Helper.MongoHelper import GetMongoClient
from Server.Model import *
from Server.Model.ModelUser import User

###############################################################################

class UserRepository():
    def __init__(self):
        self._client = GetMongoClient('User')
    async def Insert(self, item) -> bool:
        try:
            self._client.insert_one(item)
            return True
        except:
            return False
    async def Update(self, id:str=None, data=None) -> bool:
        if id and data:
            try:
                query = { "$and":[{ "_id" : ObjectId(id) }] }
                self._client.update_one(query, data)
                return True
            except:
                return False
        else:
            return False
    async def Delete(self, id:str) -> bool:
        if id:
            try:
                query = { "$and":[{ "_id" : ObjectId(id) }] }
                self._client.remove(query)
                return True
            except:
                return False
        else:
            return False
    async def Search(self, query=None) -> List[User]:
        if query:
            items = list(self._client.find(query))
            return parse_obj_as(List[User], items)
        else:
            items = list(self._client.find())
            return parse_obj_as(List[User], items)
    async def SearchOne(self, query=None) -> User:
        if query:
            item = self._client.find_one(query)
            if item != None:
                item = User.parse_obj(item)
            return item
        else:
            item = self._client.find_one()
            if item != None:
                item = User.parse_obj(item)
            return item

###############################################################################