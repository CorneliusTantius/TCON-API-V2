### Package Import ###
from fastapi.encoders import jsonable_encoder
from pymongo import message
### AppCode Import ###
import Server.Helper.HashHelper as Hash
from Server.Model.DTO.UserLoginDTO import UserLoginDTO
from Server.Model.ModelUser import *
from Server.Model.BaseOutputModel import *
from Server.Helper.Repository import *

###############################################################################

RepUser = UserRepository();

###############################################################################

async def UserRegister(parameter: User):
    try:
        # Check existing validation
        emailAndPhoneCheckQuery = { "$or": [
            {"email":parameter.Email},
            {"phoneNumber":parameter.PhoneNumber}
        ]}
        if (await RepUser.SearchOne(emailAndPhoneCheckQuery)):
            return ErrorOutputResult(message="This email or phone already exists")
        
        parameter.Password = Hash.Encode(parameter.Password)
        parameter = jsonable_encoder(parameter)
        insertResult = await RepUser.Insert(parameter)
        if insertResult:
            return OkOutputResult()
        else:
            return ErrorOutputResult()
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################

async def UserLogin(parameter: UserLoginDTO):
    try:
        print(parameter.EmailOrPhone)
        checkEmailQuery = {"$and":[{"email": parameter.EmailOrPhone}]}
        checkPhoneQuery = {"$and":[{"phoneNumber": parameter.EmailOrPhone}]}
        
        # First attempt, try to get by email
        thisUser = await RepUser.SearchOne(checkEmailQuery)
        if thisUser == None:
            thisUser = RepUser.SearchOne(checkPhoneQuery)
        
        if thisUser == None: 
            return ErrorOutputResult(message='User Not Found')
        
        decodedPass = Hash.Decode(thisUser.Password)
        if decodedPass == parameter.Password:
            return OkOutputResult()
        else: 
            return ErrorOutputResult(message='Incorrect Password')
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################