### Package Import ###
from pydantic import BaseModel
from pydantic.fields import Field
### AppCode Import ###


###############################################################################

class UserLoginDTO(BaseModel):
    EmailOrPhone:str = Field(alias='EmailOrPhone')
    Password:str = Field(alias='Password')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "EmailOrPhone":"jdoe@example.com",
                "Password":"jdoee"
            }
        }

###############################################################################



###############################################################################