from pydantic.main import BaseModel

class OkOutputModel(BaseModel):
    def __init__(self, message='Success', result={}):
        self.status = 200
        self.message = message
        self.result = result
    class Config:
        schema_extra = {
            "example": {
                "status":200,
                "message":"success",
                "result":{}
            }
        }

class ErrorOutputModel(BaseModel):
    def __init__(self, message='', result={}):
        self.status:int = 500
        self.message:str = message
        self.result:dict = result
    class Config:
        schema_extra = {
            "example": {
                "status":500,
                "message":"Error Log",
                "result":{}
            }
        }