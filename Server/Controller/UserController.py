### Package Import ###
import os
### AppCode Import ###
import Server.Helper.HashHelper as Hash
from Server.Model.ModelUser import *
from Server.Model.BaseModel import *
from Server.Helper.Repository import *

###############################################################################

RepUser = UserRepository();

###############################################################################

async def UserRegister(parameter: User):
    try:
        parameter.Password = Hash.Encode(parameter.Password)
        insertResult = await RepUser.Insert(parameter)
        if insertResult:
            return OkOutputModel()
        else:
            return ErrorOutputModel(message='Internal Server Error')
    except Exception as e:
        return ErrorOutputModel(message=str(e))

###############################################################################

async def UserLogin():
    return 'Hello World'

###############################################################################