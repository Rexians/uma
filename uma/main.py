from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.api import router as api_router
# from pydantic import BaseModel
from dotenv import load_dotenv
import os

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    '''
    Home Page to get Information, and version
    '''
    version = os.environ.get('version')
    home_dict = {
        'information': 'Unofficial MCOC API, Abbreviated as UMA, Is a API developed for MCOC Players. It has various features including Champs Info, Champs Finder and many features are being developed like Roster and Masteries. Reach out to https://indorex.gitbook.io/uma-docs for Documentation.',
        'documentation': 'https://indorex.gitbook.io/uma-docs',
        'version': version
    }
    return(home_dict)



