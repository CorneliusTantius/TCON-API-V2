### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from starlette.routing import request_response
### AppCode Import ###
import Server.Controller.ConstultantController as controller
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.ModelConsultant import ConsultantCreateModel

###############################################################################

ConsultantRoute = APIRouter()

###############################################################################

@ConsultantRoute.post('/consultant/register', description='Consultant Registration', response_model=BaseOutputModel)
async def UserRegister(parameter: ConsultantCreateModel = Body(...)):
    return await controller.ConsultantRegister(parameter)

###############################################################################