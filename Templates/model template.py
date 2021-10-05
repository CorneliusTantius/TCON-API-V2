### Package Import ###
from bson import ObjectId
from pydantic import BaseModel
from pydantic.fields import Field
from typing import Optional
### AppCode Import ###
# from .POID import PyObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

###############################################################################

class User(BaseModel):
    Id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    FirstName: str = Field(alias='firstName')
    LastName: str = Field(alias='lastName')
    Email: str = Field(alias='email')
    PhoneNumber: str = Field(alias='phoneNumber')
    Password: str = Field(alias='password')
    IsConsultant: bool = Field(alias='isConsultant')

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
                "password": "encrypted password here",
                "isConsultant": True
            }
        }

###############################################################################

class UpdateUser(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    Email: Optional[str]
    PhoneNumber: Optional[str]
    Password: Optional[str]
    IsConsultant: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "firstName": "Jane",
                "lastName": "Doe",
                "email": "jdoe@example.com",
                "phoneNumber": "6285588974456",
                "password": "encrypted password here",
                "isConsultant": True
            }
        }

###############################################################################