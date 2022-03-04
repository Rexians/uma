from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_db import NewChampsDB

router = APIRouter()

@router.get("/champs/")
def champsfunc(champ:str, tier:int, rank:int ):

    '''
    Gives Champ Information
    '''

    champ_info = NewChampsDB()
    try:
        champ_info.get_data(champ, tier, rank)
        champs_dict = {
            "name": f"{champ_info.name}",
            "prestige" : champ_info.prestige ,
            "hp" : champ_info.hp ,
            "attack" : champ_info.attack ,
            "crit_rate" : champ_info.crit_rate ,
            "crit_dmge" : champ_info.crit_dmge ,
            "armor" : champ_info.armor ,
            "block_prof" : champ_info.block_prof ,
            "energy_resist" : champ_info.energy_resist ,
            "physical_resist" : champ_info.physical_resist ,
            "crit_resist" : champ_info.crit_resist ,
            "sig_info" : f"{champ_info.sig_info}" ,
            "url_page" : f"{champ_info.url_page}",
            "img_potrait" : f"{champ_info.img_potrait}",
            "champid" : f"{champ_info.champid}",
            "status" : 200,
            "detail" : "Successful",
            }
        return(champs_dict)
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            raise HTTPException(status_code=404,detail='404: '+champ_info.error)
        elif isinstance(e, KeyError):
            raise HTTPException(status_code=400, detail='400: '+champ_info.error)
        else:
            raise e    