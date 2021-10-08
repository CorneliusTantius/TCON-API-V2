### Package Import ###
from bson import ObjectId
from pydantic import BaseModel
from pydantic import fields
from pydantic.fields import Field
from typing import Optional
### AppCode Import ###
from Server.Model.POID import PyObjectId

###############################################################################

class User(BaseModel):
    Id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    FirstName: str = Field(alias='firstName')
    LastName: str = Field(alias='lastName')
    Email: str = Field(alias='email')
    PhoneNumber: str = Field(alias='phoneNumber')
    Password: str = Field(alias='password')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "firstName": "Jane",
                "lastName": "Doe",
                "email": "jdoe@example.com",
                "phoneNumber": "6285588974456",
                "password": "jdoee"
            }
        }

###############################################################################

class UpdateUser(BaseModel):
    FirstName: Optional[str] = Field(alias ='firstName')
    LastName: Optional[str] = Field(alias='lastName')
    Email: Optional[str] = Field(alias='email')
    PhoneNumber: Optional[str] = Field(alias='phoneNumber')
    Password: Optional[str] = Field(alias='password')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "firstName": "Jane",
                "lastName": "Doe",
                "email": "jdoe@example.com",
                "phoneNumber": "6285588974456",
                "password": "jdoee"
            }
        }

###############################################################################