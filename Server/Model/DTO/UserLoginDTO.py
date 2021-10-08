### Package Import ###
from pydantic import BaseModel
from pydantic.fields import Field
### AppCode Import ###


###############################################################################

class UserLoginDTO(BaseModel):
    EmailOrPhone:str = Field(alias='emailOrPhone')
    Password:str = Field(alias='password')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "emailOrPhone":"jdoe@example.com",
                "password":"jdoee"
            }
        }

###############################################################################



###############################################################################