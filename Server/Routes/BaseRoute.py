### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
### AppCode Import ###
from Server.Model.BaseModel import OkOutputModel

###############################################################################

BaseRoute = APIRouter()

###############################################################################

@BaseRoute.get('/', description="API Entry")
async def Info():
    return OkOutputModel(message='TCON API V2.0')

###############################################################################