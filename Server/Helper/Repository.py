### Package Import ###
from typing import List
from bson import ObjectId
from pydantic import parse, parse_obj_as
from pymongo.message import _query_compressed
### AppCode Import ###
from Server.Helper.MongoHelper import GetMongoClient
from Server.Model import *
from Server.Model.ModelConsultant import Consultant, ConsultantUpdateModel
from Server.Model.ModelUser import User, UserUpdateModel

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
    async def Delete(self, Id:str) -> bool:
        if Id:
            try:
                query = { "$and":[{ "_id" : Id }] }
                self._client.delete_one(query)
                return True
            except:
                return False
        else:
            return False
    async def Search(self, query=None, pageSize=None) -> List[User]:
        if query:
            if pageSize:
                items = list(self._client.find(query).limit(pageSize))
            else:
                items = list(self._client.find(query))
            return parse_obj_as(List[User], items)
        else:
            if pageSize:
                items = list(self._client.find().limit(pageSize))
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
    async def SearchOneId(self, Id:str) -> User:
        if Id:
            query = { "$and":[{ "_id" : Id }] }
            
            item = self._client.find_one(query)
            if item != None:
                item = User.parse_obj(item)
            return item
    async def Update(self, Id:str, Data: UserUpdateModel) -> bool:
        try:
            dictionarizedData = {k: v for k, v in Data.dict().items() if v is not None}
            searchQuery = { "_id": Id }
            updateData = { "$set":dictionarizedData }
            self._client.update_one(searchQuery, updateData)
            return True
        except Exception as e:
            print(e)
            return False

###############################################################################

class ConsultantRepository():
    def __init__(self):
        self._client = GetMongoClient('Consultant')
    async def Insert(self, item) -> bool:
        try:
            self._client.insert_one(item)
            return True
        except:
            return False
    async def Delete(self, Id:str) -> bool:
        if Id:
            try:
                query = { "$and":[{ "_id" : Id }] }
                self._client.delete_one(query)
                return True
            except:
                return False
        else:
            return False
    async def Search(self, query=None, pageSize=None) -> List[Consultant]:
        if query:
            if pageSize:
                items = list(self._client.find(query).limit(pageSize))
            else:
                items = list(self._client.find(query))
            return parse_obj_as(List[Consultant], items)
        else:
            if pageSize:
                items = list(self._client.find().limit(pageSize))
            else:
                items = list(self._client.find())
            return parse_obj_as(List[Consultant], items)
    async def SearchOne(self, query=None) -> Consultant:
        if query:
            item = self._client.find_one(query)
            if item != None:
                item = Consultant.parse_obj(item)
            return item
        else:
            item = self._client.find_one()
            if item != None:
                item = Consultant.parse_obj(item)
            return item
    async def SearchOneId(self, Id:str) -> Consultant:
        if Id:
            query = { "$and":[{ "_id" : Id }] }
            
            item = self._client.find_one(query)
            if item != None:
                item = Consultant.parse_obj(item)
            return item
    async def Update(self, Id:str, Data: ConsultantUpdateModel) -> bool:
        try:
            dictionarizedData = {k: v for k, v in Data.dict().items() if v is not None}
            searchQuery = { "_id": Id }
            updateData = { "$set":dictionarizedData }
            self._client.update_one(searchQuery, updateData)
            return True
        except Exception as e:
            print(e)
            return False

###############################################################################



###############################################################################
