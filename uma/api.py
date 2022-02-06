from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from selenium.common.exceptions import NoSuchElementException
from src.mcoc_find import champs_detailed
from src.mcoc_db import ChampsDB
from src.mcoc_roster import Roster
from pydantic import BaseModel

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

@app.get("/champs/")
def champsfunc(champ:str, tier:int ):

    '''
    Gives Champ Info
    '''

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
 
@app.get("/roster/create")
def roster_createfunc(gamename:str):
    roster.create_roster(gamename)
    if roster.error == 'None':
        detail = {
            'status':200,
            'detail':'Successful',
            }
        return(detail)
    else:
        raise HTTPException(status_code=404, detail=roster.error)  

@app.get("/roster/get")
def roster_getfunc(gamename:str):
    roster.get_roster(gamename)
    if roster.error == 'None':
        roster_dict = roster.roster_dict
        roster_dict['status']=200
        roster_dict['detail']='Successful'
        return(roster_dict)
    else:
        raise HTTPException(status_code=404, detail=roster.error)    

@app.get("/roster/addchamp")
def roster_updatefunc(gamename:str, champname:str, tier:int, signature:int):

    champnameurl = champname
    if champname == "bwcv":
        champnameurl="blackwidow_timely"
    elif champname == "redgoblin":
        champnameurl="red_goblin"        
    elif champname == "bwdo":
        champnameurl="blackwidow_movie"
    elif champname == "ultron":
        champnameurl="ultron_prime"    
    elif champname == "ultronlol":
        champnameurl="ultron"        
    elif champname == "spidersymbiote":
        champnameurl="spiderman_black"
    elif champname == "mordo":
        champnameurl="karlmordo"    
    elif champname == "sorcerersupreme":
        champnameurl="drstrange_realm"  
    elif champname == "oml":
        champnameurl="wolverine_oldman"          
    elif champname == "hulkbuster":
        champnameurl="hulkbuster_movie"
    elif champname == "ironfistimmortal":
        champnameurl="ironfist_white"        
    elif champname == "cyclops_blue":
        champnameurl="cyclops_90s"        
    elif champname == "cmm":
        champnameurl="captainmarvel_movie"
    elif champname == "caiw":
        champnameurl="captainamerica_movie"
    elif champname == "caww2":
        champnameurl="captainamerica_ww2"        
    elif champname == "imiw":
        champnameurl="ironman_movie"
    elif champname == "jabaripanther":
        champnameurl="blackpanther_realm"
    elif champname =="kinggroot":
        champnameurl="groot_king"
    elif champname =="misterfantastic":
        champnameurl="mrfantastic"
    elif champnameurl =="bpcw":
        champnameurl="blackpanther_cw"
    elif champname=="punisher2099":
        champnameurl="punisher_2099"
    elif champname=="rocketracoon":
        champnameurl="rocket"
    elif champname=="spiderman2099":
        champnameurl="spiderman_2099"
    elif champname=="overseer":
        champnameurl="maestro_overseer"
    elif champname=="unstoppablecolossus" :
        champnameurl="colossus_unstoppable"
    elif champname=="visionaarkus":
        champnameurl=="vision_timely"
    elif champname=="visionmovie":
        champnameurl="vision_movie"
    elif champname=="vulture":
        champnameurl="vulture_movie"
    elif champname=="wolverinex":
        champnameurl="wolverine_weaponx"
    elif champname=="spidermorales":
        champnameurl="spiderman_morales"
    elif champname=="starkspiderman":
        champnameurl="spiderman_movie"
    elif champname=="spiderstealth ":
        champnameurl="spiderman_stealth"
    elif champname=="redmagneto":
        champnameurl="magneto"
    elif champname=="magnetowhite":
        champnameurl="magneto_marvelnow" 
    elif champname=="kamalakhan":
        champnameurl="msmarvel_kamala"
    elif champname=="platinumpool":
        champnameurl="deadpool_platinumpool"
    elif champname=="scarletwitchnew":
        champnameurl="scarletwitch_current"
    elif champname=="silvercenturion":
        champnameurl="ironman_silvercenturion"
    elif champname=="stormpyramidx":
        champnameurl="storm_realm"
    elif champname=="superskrull":
        champnameurl="skrull_super"
    elif champname=="superiorironman":
        champnameurl="ironman_superior"
    elif champname=="janefoster":
        champnameurl="thor_janefoster"                                        
    elif champname=="thorragnarok":
        champnameurl="thor_ragnarok"
    elif champname=="ibom":
        champnameurl="abomination_immortal"
    elif champname=="doctorvoodoo":
        champnameurl="brothervoodoo"
    elif champname=="daredevil netflix":
        champnameurl="daredevil_netflix"
    elif champname=="goldpool":
        champnameurl="deadpool_goldpool"
    elif champname=="cgr":
        champnameurl="ghostrider_cosmic"
    elif champname=="docock":
        champnameurl="doc_ock"
    elif champname=="greengoblin":
        champnameurl="green_goblin"
    elif champname=="howard":
        champnameurl="howardmech"

    roster.add_champ(gamename, champnameurl, tier, signature)
    if roster.error == 'None':
        detail = {
            'status':200,
            'detail':'Successful',
            }
        return(detail)    
    else:
        raise HTTPException(status_code=404, detail=roster.error)   

class BulkUpdate(BaseModel):
    gamename: str
    roster_dict: list

@app.post('/roster/bulkadd')
def roster_bulkfunc(roster_bulk:BulkUpdate):
    roster.bulk_add(roster_bulk.gamename, roster_bulk.roster_dict)
    if roster.error == 'None':
        detail = {
            'status':200,
            'detail':'Successful',
            }
        return(detail)
    else:
        raise HTTPException(status_code=404, detail=roster.error)   

