### Package Import ###
from fastapi.encoders import jsonable_encoder
### AppCode Import ###
import Server.Helper.HashHelper as Hash
from Server.Model.DTO.UserLoginDTO import UserLoginDTO
from Server.Model.ModelUser import *
from Server.Model.BaseOutputModel import *
from Server.Helper.Repository import *

###############################################################################

RepUser = UserRepository()

###############################################################################

async def UserRegister(parameter: User):
    try:
        # Check existing validation
        emailAndPhoneCheckQuery = { "$or": [
            {"Email":parameter.Email},
            {"PhoneNumber":parameter.PhoneNumber}
        ]}
        if (await RepUser.SearchOne(emailAndPhoneCheckQuery)):
            return ErrorOutputResult(message="This email or phone already exists")
        
        insertion = parameter
        insertion.Password = Hash.Encode(insertion.Password)
        insertion = jsonable_encoder(insertion)
        insertResult = await RepUser.Insert(insertion)
        if insertResult:
            parameter.Password = 'Encrypted Value'
            return OkOutputResult(result=parameter)
        else:
            return ErrorOutputResult()
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################

async def UserLogin(parameter: UserLoginDTO):
    try:
        checkEmailQuery = {"$and":[{"Email": parameter.EmailOrPhone}]}
        checkPhoneQuery = {"$and":[{"PhoneNumber": parameter.EmailOrPhone}]}
        
        # First attempt, try to get by email
        thisUser = await RepUser.SearchOne(checkEmailQuery)
        if thisUser == None:
            thisUser = RepUser.SearchOne(checkPhoneQuery)
        
        if thisUser == None: 
            return ErrorOutputResult(message='User Not Found')
        
        decodedPass = Hash.Decode(thisUser.Password)
        if decodedPass == parameter.Password:
            thisUser.Password = 'Encrypted Value'
            return OkOutputResult(result=jsonable_encoder(thisUser))
        else: 
            return ErrorOutputResult(message='Incorrect Password')
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################

async def UserUpdate(Id: str, parameter: UserUpdateModel):
    try:
        if parameter.Password != None:
            parameter.Password = Hash.Encode(parameter.Password)
        result = await RepUser.Update(Id = Id, Data = parameter)
        if result:
            return OkOutputResult(message='Data Updated')
        else:
            return ErrorOutputResult()
    except Exception as e:
        return ErrorOutputResult(message=str(e))