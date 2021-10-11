### Package Import ###
from bson import ObjectId
from pydantic import BaseModel
from pydantic import fields
from pydantic.fields import Field
from typing import Optional
### AppCode Import ###
from Server.Model.POID import PyObjectId

###############################################################################

class Consultant(BaseModel):
    Id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    FirstName: str = Field(alias='FirstName')
    LastName: str = Field(alias='LastName')    
    Email: str = Field(alias='Email')
    PhoneNumber: str = Field(alias='PhoneNumber')
    Password: str = Field(alias='Password')
    Category: str = Field(alias = 'Category')
    Bio: str = Field(alias = 'Bio')
    Experience: str = Field(alias = 'Experience')
    Awards: str = Field(alias = 'Awards')
    Education: str = Field(alias = 'Education')
    Rating: float = Field(alias = 'Rating')
    RatingCount: int = Field(alias = 'RatingCount')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "FirstName": "Jane",
                "LastName": "Doe",
                "Email": "jdoe@example.com",
                "PhoneNumber": "6285588974456",
                "Password": "jdoee",
                "Category": "technology",
                "Bio": "html embed",
                "Experience": "html embed",
                "Awards": "html embed",
                "Education": "html embed",
                "Rating": 4.5,
                "RatingCount": 122
            }
        }

###############################################################################

class ConsultantUpdateModel(BaseModel):
    FirstName: Optional[str] = Field(alias ='FirstName')
    LastName: Optional[str] = Field(alias='LastName')
    Email: Optional[str] = Field(alias='Email')
    PhoneNumber: Optional[str] = Field(alias='PhoneNumber')
    Password: Optional[str] = Field(alias='Password')
    Category: Optional[str] = Field(alias = 'Category')
    Bio: Optional[str] = Field(alias = 'Bio')
    Experience: Optional[str] = Field(alias = 'Experience')
    Awards: Optional[str] = Field(alias = 'Awards')
    Education: Optional[str] = Field(alias = 'Education')
    Rating: Optional[float] = Field(alias = 'Rating')
    RatingCount: Optional[int] = Field(alias = 'RatingCount')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "FirstName": "Jane",
                "LastName": "Doe",
                "Email": "jdoe@example.com",
                "PhoneNumber": "6285588974456",
                "Password": "jdoee",
                "Category": "technology",
                "Bio": "html embed",
                "Experience": "html embed",
                "Awards": "html embed",
                "Education": "html embed",
                "Rating": 4.5,
                "RatingCount": 122
            }
        }

###############################################################################