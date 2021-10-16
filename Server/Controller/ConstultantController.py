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
