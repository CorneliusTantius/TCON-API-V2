### Package Import ###
from bson import ObjectId
from pydantic import BaseModel
from pydantic import fields
from pydantic.fields import Field
from typing import List, Optional
### AppCode Import ###
from Server.Model.POID import PyObjectId

###############################################################################

class Ticket(BaseModel):
    Id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    CreatedDate: str = Field(alias='CreatedDate')
    DueDate: str = Field(alias='DueDate')
    Priority: int = Field(alias='Priority')
    UserId: str = Field(alias='UserId')
    Subject: str = Field(alias='Subject')
    Description: str = Field(alias='Description')
    IsResolved: bool = Field(alias='IsResolved')
    ThumnailUrl: str = Field(alias='ThumbnailUrl')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "CreatedDate": "26-10-2021",
                "DueDate": "23-02-2022",
                "Priority": 1,
                "UserId": "userId",
                "Subject": "BSOD",
                "Description": "my laptop got bsod",
                "IsResolved": False,
                "ThumbnailUrl": "www.google.com"
            }
        }

###############################################################################



###############################################################################