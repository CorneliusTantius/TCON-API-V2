### Package Import ###
from bson import ObjectId
from pydantic import BaseModel
from pydantic import fields
from pydantic.fields import Field
from typing import List, Optional
### AppCode Import ###
from Server.Model.POID import PyObjectId

###############################################################################

class LikeAndView(BaseModel):
    Id: str = Field(alias='Id')
    IsUser: bool = Field(alias='IsUser')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "Id":"user/consultant Id",
            "IsUser":True
        }

class Comment(BaseModel):
    Id: str = Field(alias='Id')
    IsUser: bool = Field(alias='IsUser')
    CommentStr: str = Field(alias='CommentStr')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "Id":"user/consultant Id",
            "IsUser":True,
            "CommentStr":""
        }

###############################################################################

class Blog(BaseModel):
    Id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    CreatedDate: str = Field(alias='CreatedDate')
    Title: str = Field(alias='Title')    
    UserId: str = Field(alias='UserId')
    ConsultantId: str = Field(alias='ConsultantId')
    IsUser: bool = Field(alias='IsUser')
    Content: str = Field(alias = 'Content')
    LikesCount: List[LikeAndView] = Field(alias = 'LikesCount')
    ViewsCount: List[LikeAndView] = Field(alias = 'ViewsCount')
    CommentsList: List[Comment] = Field(alias = 'CommentsList')
    ThumbnailUrl: str = Field(alias = 'ThumbnailUrl')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "CreatedDate": "26-10-2021",
                "Title": "title",
                "UserId": "id",
                "ConsultantId": "id",
                "IsUser": False,
                "Content": "article content",
                "LikesCount": [LikeAndView.Config.schema_extra],
                "ViewsCount": [LikeAndView.Config.schema_extra],
                "CommentsList": [Comment.Config.schema_extra],
                "ThumbnailUrl": "www.google.com"
            }
        }

###############################################################################



###############################################################################