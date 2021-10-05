### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
### AppCode Import ###
from Server.Model.BaseOutputModel import *

###############################################################################

BaseRoute = APIRouter()

###############################################################################

@BaseRoute.get('/', description="API Entry", response_model=BaseOutputModel)
async def Info():
    return OkOutputResult(message='TCON API V2.0')

###############################################################################