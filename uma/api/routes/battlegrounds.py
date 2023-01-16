from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_battlegrounds import Battlegrounds

router = APIRouter()

@router.get("/battlegrounds/season/{season}")
def get_battlegrounds_info(season):

    """
    Get information of battlegrounds based on season
    """
    print(type(season))
    battlegrounds = Battlegrounds() 
    battlegrounds.read_battleground_data(int(season))
    if battlegrounds.error == None:
        battlegrounds_dict = {
            "start": battlegrounds.start,
            "end": battlegrounds.end,
            "season": battlegrounds.season,
            "victory_track": battlegrounds.victory_track,
            "gladiator_circuit": battlegrounds.gladiator_circuit,
            "status": 200,
            "detail": "Successful",
        }
        return battlegrounds_dict
    else:
        raise HTTPException(400, battlegrounds.error)