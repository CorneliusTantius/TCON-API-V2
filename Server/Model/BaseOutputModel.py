from pydantic import BaseModel
from pydantic.fields import Field

class BaseOutputModel(BaseModel):
    status:int = 0
    message:str = ''
    result:dict = {}

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "status":200,
                "message":"success",
                "result":{}
            }
        }

def OkOutputResult(message='Success', result={}):
    retVal = BaseOutputModel()
    retVal.status = 200
    retVal.message = message
    retVal.result = result
    return retVal

def ErrorOutputResult(message='Internal Server Error', result={}):
    retVal = BaseOutputModel()
    retVal.status = 500
    retVal.message = message
    retVal.result = result
    return retVal