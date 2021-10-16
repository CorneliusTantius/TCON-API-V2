### Package Import ###
from os import replace
from fastapi.encoders import jsonable_encoder
from pymongo.message import insert
from Server.Controller.UserController import RepUser
### AppCode Import ###
import Server.Helper.HashHelper as Hash
from Server.Helper.Repository import *
from Server.Model.BaseOutputModel import *
from Server.Model.ModelConsultant import ConsultantCreateModel
from Server.Model.DTO.UserLoginDTO import UserLoginDTO

###############################################################################

RepConsultant = ConsultantRepository()

###############################################################################

async def ConsultantRegister(parameter: ConsultantCreateModel):
    try:
        emailAndPhoneCheckQuery = { "$or": [
            {"Email":parameter.Email},
            {"PhoneNumber":parameter.PhoneNumber}
        ]}
        if (await RepConsultant.SearchOne(emailAndPhoneCheckQuery)):
            return ErrorOutputResult(message="This email of phone already exists")
        
        insertion = Consultant()
        insertion.FirstName = parameter.FirstName
        insertion.LastName = parameter.LastName
        insertion.Email = parameter.Email
        insertion.PhoneNumber = parameter.PhoneNumber
        insertion.Password = Hash.Encode(parameter.Password)
        insertion.Category = []
        insertion.Bio = ""
        insertion.Experience = ""
        insertion.Awards = []
        insertion.Educations = []
        insertion.Rating = 5.0
        insertion.RatingCount = 1

        insertion_json = jsonable_encoder(insertion)
        insertResult = await RepConsultant.Insert(insertion_json)
        if insertResult:
            insertion.Password = 'Ecrypted Value'
            return OkOutputResult(result=insertion)
        else:
            return ErrorOutputResult()
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################

async def ConsultantLogin(parameter: UserLoginDTO):
    try:
        checkEmailQuery = {"$and":[{"Email": parameter.EmailOrPhone}]}
        checkPhoneQuery = {"$and":[{"PhoneNumber": parameter.EmailOrPhone}]}
        
        # First attempt, try to get by email
        thisUser = await RepConsultant.SearchOne(checkEmailQuery)
        if thisUser == None:
            thisUser = RepConsultant.SearchOne(checkPhoneQuery)
        
        if thisUser == None: 
            return ErrorOutputResult(message='Consultant Not Found')
        
        decodedPass = Hash.Decode(thisUser.Password)
        if decodedPass == parameter.Password:
            thisUser.Password = 'Encrypted Value'
            return OkOutputResult(result=jsonable_encoder(thisUser))
        else: 
            return ErrorOutputResult(message='Incorrect Password')
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################

async def ConsultantUpdateDetails(Id:str, parameter: ConsultantUpdateModel):
    try:
        if parameter.Password != None:
            parameter.Password = Hash.Encode(parameter.Password)
        result = await RepConsultant.Update(Id = Id, Data = parameter)
        if result:
            return OkOutputResult(message='Data Updated')
        else:
            return ErrorOutputResult()
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################