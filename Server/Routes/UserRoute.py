### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from starlette.routing import request_response
### AppCode Import ###
import Server.Controller.UserController as controller
from Server.Model.BaseModel import OkOutputModel
from Server.Model.ModelUser import *

###############################################################################

UserRoute = APIRouter()

###############################################################################

@UserRoute.post('/user/register', description='User Registration', response_model=OkOutputModel)
async def UserRegister(parameter: User = Body(...)):
    return await controller.UserRegister(parameter)

@UserRoute.post('/user/login', description='User Login')
async def UserLogin():
    return await controller.UserLogin()

###############################################################################