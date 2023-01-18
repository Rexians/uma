import os

from api.routes import champ_info, find, nodes, roster, war
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets/portraits", StaticFiles(directory="files/portraits"), name="static")
app.include_router(champ_info.router)
app.include_router(roster.router)
app.include_router(nodes.router)
app.include_router(war.router)
app.include_router(find.router)
app.include_router(battlegrounds.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    errors = exc.errors()
    error_content = "The following arguments are missing: "
    for error in errors:
        if error["type"] == "value_error.missing":
            field = f"{error['loc'][1]},"
            error_content += field
    error_content = error_content.removesuffix(",")

    return JSONResponse({"detail": error_content}, status_code=422)


@app.get("/")
def home():
    """
    Home Page to get Information, and version
    """
    version = "5.2.2"
    home_dict = {
        "information": "Unofficial MCOC API, Abbreviated as UMA, Is a API developed for MCOC Players. It has various features including Champs Info, Champs Finder and many features are being developed like Roster and Masteries. Reach out to https://docs.rexians.tk/ for Documentation.",
        "documentation": "https://docs.rexians.tk/",
        "version": version,
    }
    return home_dict
