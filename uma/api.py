from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from selenium.common.exceptions import NoSuchElementException
from src.mcoc_find import champs_detailed
from src.mcoc_db import ChampsDB
from src.mcoc_roster import Roster
from pydantic import BaseModel
from dotenv import load_dotenv
import os

app = FastAPI()
find = champs_detailed()
info = ChampsDB()
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
def champsfunc(champ:str, tier:int ):

    '''
    Gives Champ Info
    '''

    champurl = champurl_getter(champ)

    try:
        info.champs_info(champurl,tier)
        champs_dict = {
            "name": f"{info.name}",
            "prestige" : f"{info.prestige}" ,
            "hp" : f"{info.hp}" ,
            "attack" : f"{info.attack}" ,
            "crit_rate" : f"{info.crit_rate}" ,
            "crit_dmge" : f"{info.crit_dmge}" ,
            "armor" : f"{info.armor}" ,
            "block_prof" : f"{info.block_prof}" ,
            "energy_resist" : f"{info.energy_resist}" ,
            "physical_resist" : f"{info.physical_resist}" ,
            "crit_resist" : f"{info.crit_resist}" ,
            "sig_info" : f"{info.sig_info}" ,
            "url_page" : f"{info.url_page}",
            "img_potrait" : f"{info.link}",
            "champid" : f"{info.champid}",
            "status" : 200,
            "detail" : "Successful",
            }

        return(champs_dict)
    except NoSuchElementException:
        raise HTTPException(status_code=404,detail='Error on Finding Champ/Element on AUNTM.ai and/or Database')
 
@app.get("/find/")
def findfunc(champ:str):

    '''
    Tells where a champ can be found
    '''

    champurl = champurl_getter(champ)   

    try:

        find.champs_find(f"{champurl}")
        champs_dict = {
            "name": f"{find.name}",
            "url_page" : f"{find.url_page}",
            "img_potrait" : f"{find.img_potrait}",
            "quests":{
                "story_quests": f'{find.story_quest}',
                "event_quests": f'{find.event_quest}',
                "alliance_quests": f'{find.alliance_quest}',
                "incursions": f'{find.incursions}',
                "daily_quests": f'{find.daily_quests}',
                "special_quests": f'{find.special_quests}',
                "back_quests": f'{find.back_quests}'
                },

            "champid" : f"{champ}",
            "status" : 200,
            "detail" : "Successful",
            }

        return(champs_dict)
    except NoSuchElementException:
        raise HTTPException(status_code=404,detail='Error on Finding Champ/Element on AUNTM.ai')

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

@app.get("/roster/addchamp")
def roster_updatefunc(gamename:str, champname:str, tier:int, signature:int):
    '''
    Add/Update Roster in Database
    '''
    champnameurl = champurl_getter(champname)

    roster.add_champ(gamename, champnameurl, tier, signature)
    if roster.error == '':
        detail = {
            'status':200,
            'detail':roster.details,
            }
        return(detail)    
    else:
        raise HTTPException(status_code=404, detail=roster.error)   

#Heavily Bugged Feature! Still developing...
class BulkUpdate(BaseModel):
    gamename: str
    roster_dict: list

@app.post('/roster/bulkadd')
def roster_bulkfunc(roster_bulk:BulkUpdate):
    roster.bulk_add(roster_bulk.gamename, roster_bulk.roster_dict)
    if roster.error == '':
        detail = {
            'status':200,
            'detail':'Successful',
            }
        return(detail)
    else:
        raise HTTPException(status_code=404, detail=roster.error)   

