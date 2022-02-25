from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.mcoc_find import champs_detailed
from src.mcoc_db import NewChampsDB
from src.mcoc_roster import Roster
from pydantic import BaseModel
from dotenv import load_dotenv
import os

async def not_found(request, exc):
    return JSONResponse(content={'detail':'404: Route not found!'}, status_code=exc.status_code)

exceptions = {
    404: not_found,
}
app = FastAPI(exception_handlers=exceptions)
find = champs_detailed()
info = NewChampsDB()
roster = Roster()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def champurl_getter(champ):
    champurl = champ

    if champ == "bwcv":
        champurl="blackwidow_timely"
    elif champ == "redgoblin":
        champurl="red_goblin"        
    elif champ == "bwdo":
        champurl="blackwidow_movie"
    elif champ == "ultron":
        champurl="ultron_prime"    
    elif champ == "ultronlol":
        champurl="ultron"        
    elif champ == "spidersymbiote":
        champurl="spiderman_black"
    elif champ == "mordo":
        champurl="karlmordo"    
    elif champ == "sorcerersupreme":
        champurl="drstrange_realm"  
    elif champ == "oml":
        champurl="wolverine_oldman"          
    elif champ == "hulkbuster":
        champurl="hulkbuster_movie"
    elif champ == "ironfistimmortal":
        champurl="ironfist_white"        
    elif champ == "cyclops_blue":
        champurl="cyclops_90s"        
    elif champ == "cmm":
        champurl="captainmarvel_movie"
    elif champ == "caiw":
        champurl="captainamerica_movie"
    elif champ == "casw":
        champurl = "captainamerica_samwilson"    
    elif champ == "caww2":
        champurl="captainamerica_ww2"        
    elif champ == "imiw":
        champurl="ironman_movie"
    elif champ == "jabaripanther":
        champurl="blackpanther_realm"
    elif champ =="kinggroot":
        champurl="groot_king"
    elif champ =="misterfantastic":
        champurl="mrfantastic"
    elif champurl =="bpcw":
        champurl="blackpanther_cw"
    elif champ=="punisher2099":
        champurl="punisher_2099"
    elif champ=="rocketracoon":
        champurl="rocket"
    elif champ=="spiderman2099":
        champurl="spiderman_2099"
    elif champ=="overseer":
        champurl="maestro_overseer"
    elif champ=="unstoppablecolossus" :
        champurl="colossus_unstoppable"
    elif champ=="visionaarkus":
        champurl=="vision_timely"
    elif champ=="visionmovie":
        champurl="vision_movie"
    elif champ=="vulture":
        champurl="vulture_movie"
    elif champ=="wolverinex":
        champurl="wolverine_weaponx"
    elif champ=="spidermorales":
        champurl="spiderman_morales"
    elif champ=="starkspiderman":
        champurl="spiderman_movie"
    elif champ=="spiderstealth ":
        champurl="spiderman_stealth"
    elif champ=="redmagneto":
        champurl="magneto"
    elif champ=="magnetowhite":
        champurl="magneto_marvelnow" 
    elif champ=="kamalakhan":
        champurl="msmarvel_kamala"
    elif champ=="platinumpool":
        champurl="deadpool_platinumpool"
    elif champ=="scarletwitchnew":
        champurl="scarletwitch_current"
    elif champ=="silvercenturion":
        champurl="ironman_silvercenturion"
    elif champ=="stormpyramidx":
        champurl="storm_realm"
    elif champ=="superskrull":
        champurl="skrull_super"
    elif champ=="superiorironman":
        champurl="ironman_superior"
    elif champ=="janefoster":
        champurl="thor_janefoster"                                        
    elif champ=="thorragnarok":
        champurl="thor_ragnarok"
    elif champ=="ibom":
        champurl="abomination_immortal"
    elif champ=="doctorvoodoo":
        champurl="brothervoodoo"
    elif champ=="daredevil netflix":
        champurl="daredevil_netflix"
    elif champ=="goldpool":
        champurl="deadpool_goldpool"
    elif champ=="cgr":
        champurl="ghostrider_cosmic"
    elif champ=="docock":
        champurl="doc_ock"
    elif champ=="greengoblin":
        champurl="green_goblin"
    elif champ=="howard":
        champurl="howardmech"
    return(champurl)    

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

@app.get("/champs/")
def champsfunc(champ:str, tier:int, rank:int ):

    '''
    Gives Champ Info
    '''

    champurl = champurl_getter(champ)

    try:
        info.get_data(champ, tier, rank)
        champs_dict = {
            "name": f"{info.name}",
            "prestige" : info.prestige ,
            "hp" : info.hp ,
            "attack" : info.attack ,
            "crit_rate" : info.crit_rate ,
            "crit_dmge" : info.crit_dmge ,
            "armor" : info.armor ,
            "block_prof" : info.block_prof ,
            "energy_resist" : info.energy_resist ,
            "physical_resist" : info.physical_resist ,
            "crit_resist" : info.crit_resist ,
            "sig_info" : f"{info.sig_info}" ,
            "url_page" : f"{info.url_page}",
            "img_potrait" : f"{info.img_potrait}",
            "champid" : f"{info.champid}",
            "status" : 200,
            "detail" : "Successful",
            }
        return(champs_dict)
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            raise HTTPException(status_code=404,detail='404: '+info.error)
        elif isinstance(e, KeyError):
            raise HTTPException(status_code=400, detail='400: '+info.error)
        else:
            raise e    

@app.get("/roster/get")
def roster_getfunc(gamename:str):
    '''
    Get Roster Details
    '''
    roster.get_roster(gamename)
    if roster.error == '':
        roster_dict = roster.roster_dict
        roster_dict['status']=200
        roster_dict['detail']='Successful'
        return(roster_dict)
    else:
        raise HTTPException(status_code=404, detail=roster.error)    



