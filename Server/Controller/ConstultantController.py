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
        if (await RepConsultant.SearchOne(emailAndPhoneCheckQuery) != None):
            return ErrorOutputResult(message="This email of phone already exists")
        
        insertion = Consultant(
            FirstName = parameter.FirstName,
            LastName = parameter.LastName,
            Email = parameter.Email,
            PhoneNumber = parameter.PhoneNumber,
            Password = Hash.Encode(parameter.Password),
            Category = parameter.Category,
            Bio = "",
            Experience = "",
            Awards = [],
            Educations = [],
            Rating = 5.0,
            RatingCount = 1
        )

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
            thisUser = await RepConsultant.SearchOne(checkPhoneQuery)
        
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

async def GetConsultantLimit(PageSize:int):
    try:
        datas = await RepConsultant.Search(pageSize=PageSize)
        if datas == None:
            return OkOutputResult(result=[])
        else:
            ret = []
            keys = ["_id", "FirstName", "LastName", "Category", "Rating", "RatingCount"]
            for data in datas:
                ret.append(dict((k, data[k]) for k in keys if k in data) )
            return OkOutputResult(result=datas)
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################

async def GetConsultantDetail(Id:str):
    try:
        data = await RepConsultant.SearchOneId(Id)
        if data == None:
            return ErrorOutputResult(message="Consultant not found")
        else:
            data.Password = "Encrypted Value"
            return OkOutputResult(result=jsonable_encoder(data))
        return
    except Exception as e:
        return ErrorOutputResult(message=str(e))

###############################################################################