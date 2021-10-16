### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from starlette.routing import request_response
### AppCode Import ###
import Server.Controller.ConstultantController as controller
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.ModelConsultant import ConsultantCreateModel, ConsultantUpdateModel

###############################################################################

ConsultantRoute = APIRouter()

###############################################################################

@ConsultantRoute.post('/consultant/register', description='Consultant Registration', response_model=BaseOutputModel)
async def UserRegister(parameter: ConsultantCreateModel = Body(...)):
    return await controller.ConsultantRegister(parameter)

@ConsultantRoute.post('/consultant/login', description='Consultant Login', response_model=BaseOutputModel)
async def UserRegister(parameter: ConsultantCreateModel = Body(...)):
    return await controller.ConsultantLogin(parameter)

@ConsultantRoute.post('/consultant/update/{Id}', description='Consultant Update', response_model=BaseOutputModel)
async def UserLogin(Id: str, parameter: ConsultantUpdateModel = Body(...)):
    return await controller.ConsultantUpdateDetails(Id, parameter)

@ConsultantRoute.get('/consultant/get/limit/{PageSize}', description='Get Consultant with n limit', response_model=BaseOutputModel)
async def UserLogin(PageSize:int):
    return await controller.GetConsultantLimit(PageSize=PageSize)

@ConsultantRoute.get('/consultant/get/detail/id/{Id}', description='Get Consultant Detail with Id', response_model=BaseOutputModel)
async def UserLogin(Id:str):
    return await controller.GetConsultantDetail(Id=Id)

###############################################################################