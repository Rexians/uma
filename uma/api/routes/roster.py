from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_roster import Roster

# from pydantic import BaseModel
from dotenv import load_dotenv
import os

router = APIRouter()


@router.get("/roster/get/")
def get_roster(gamename: str):
    """
    Get Roster Details of a user by Gamename
    """
    print(gamename)
    roster = Roster()
    roster.get_roster(gamename)
    if roster.error == "":
        roster_dict = roster.roster_dict
        roster_dict["status"] = 200
        roster_dict["detail"] = "Successful"
        return roster_dict
    else:
        raise HTTPException(status_code=404, detail=roster.error)
