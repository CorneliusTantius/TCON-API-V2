### Package Import ###
import os
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
### AppCode Import ###
from Server.Routes import *
from Server.Routes.BaseRoute import BaseRoute
from Server.Routes.ConsultantRoute import ConsultantRoute
from Server.Routes.UserRoute import UserRoute

###############################################################################

os.system("pyclean . -q")
program = FastAPI()
security = HTTPBearer()

###############################################################################

program.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###############################################################################

program.include_router(BaseRoute)
program.include_router(UserRoute)
program.include_router(ConsultantRoute)

###############################################################################

os.system("pyclean . -q")