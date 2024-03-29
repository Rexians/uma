from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_db import NewChampsDB

router = APIRouter()
champ_info = NewChampsDB()


@router.get("/champs/")
def get_champ_data(champ: str, tier: int, rank: int):

    """
    Gives Champ Information by their champname, tier, and rank.
    """

    try:
        champ_info.get_data(champ, tier, rank)
        champs_dict = {
            "name": f"{champ_info.name}",
            "released": champ_info.released,
            "class": champ_info.class_type,
            "tier": champ_info.tier,
            "rank": champ_info.rank,
            "prestige": champ_info.prestige,
            "hp": champ_info.hp,
            "attack": champ_info.attack,
            "crit_rate": champ_info.crit_rate,
            "crit_dmge": champ_info.crit_dmge,
            "armor": champ_info.armor,
            "block_prof": champ_info.block_prof,
            "energy_resist": champ_info.energy_resist,
            "physical_resist": champ_info.physical_resist,
            "crit_resist": champ_info.crit_resist,
            "sig_info": champ_info.sig_info,
            "abilities": champ_info.abilities,
            "challenger_rating": champ_info.challenger_rating,
            "find": champ_info.find,
            "tags": champ_info.tags,
            "abilities": champ_info.abilities,
            "contact": champ_info.contact,
            "url_page": f"{champ_info.url_page}",
            "img_portrait": f"{champ_info.img_portrait}",
            "champid": f"{champ_info.champid}",
        }

        champs_dict.update({"status": 200, "detail": "Successful"})

        return champs_dict

    except Exception as e:
        if isinstance(e, FileNotFoundError):
            raise HTTPException(status_code=404, detail="404: " + champ_info.error)
        elif isinstance(e, KeyError):
            raise HTTPException(status_code=400, detail="400: " + champ_info.error)
        else:
            raise e

@router.get("/champs/all")
def get_all_champs_data():
    '''
    Get Information of every tier of every champ present in the database.
    '''
    try:
        return champ_info.get_whole_data()
    except:
        raise HTTPException(status_code=404, detail="404")
