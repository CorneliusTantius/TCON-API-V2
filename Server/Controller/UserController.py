### Package Import ###
from fastapi.encoders import jsonable_encoder
### AppCode Import ###
import Server.Helper.HashHelper as Hash
from Server.Model.ModelUser import *
from Server.Model.BaseOutputModel import *
from Server.Helper.Repository import *

###############################################################################

RepUser = UserRepository();

###############################################################################

async def UserRegister(parameter: User):
    try:
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

async def UserLogin():
    return 'Hello World'

###############################################################################