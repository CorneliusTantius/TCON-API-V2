### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from starlette.routing import request_response
### AppCode Import ###
import Server.Controller.UserController as controller
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.DTO.UserLoginDTO import UserLoginDTO
from Server.Model.ModelUser import *

###############################################################################

UserRoute = APIRouter()

###############################################################################

@UserRoute.post('/user/register', description='User Registration', response_model=BaseOutputModel)
async def UserRegister(parameter: User = Body(...)):
    return await controller.UserRegister(parameter)

@UserRoute.post('/user/login', description='User Login', response_model=BaseOutputModel)
async def UserLogin(parameter: UserLoginDTO = Body(...)):
    return await controller.UserLogin(parameter)

###############################################################################