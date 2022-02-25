import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

    
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

class ChampsDB:
    '''
    Class for getting Champs Info'''
    def __init__(self):
        self.prestige = None
        self.hp = None
        self.attack = None
        self.crit_rate = None
        self.crit_dmge = None
        self.armor = None
        self.block_prof = None
        self.energy_resist = None
        self.physical_resist = None
        self.crit_resist = None
        self.sig_info = None
        self.url_page = None
        self.img_potrait = None
        self.name = None
        self.link =  None
        self.error = None
        self.champid = None

    def champs_info(self, champname:str, tier_str:int):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["ChampsInfo"]  
        info = f"{champname}+{tier_str}"
        x = db.find_one({"champid":info})
        if x is None:      
            try:
                url = f"https://auntm.ai/champions/{champname}/tier/{tier_str}"
                opts = webdriver.ChromeOptions()
                opts.add_argument("--no-sandbox");
                opts.add_argument("--disable-dev-shm-usage");
                opts.add_argument(" --headless");
                opts.add_argument("--disable-gpu")        
                browser = webdriver.Chrome(options=opts)
                browser.get(url)
                name_acc = browser.find_element(By.CSS_SELECTOR, '.sc-bZSQDF')
                link_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-bkzZxe:nth-child(1) > img:nth-child(1) ').get_attribute("src")
                prestige_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(9) > div:nth-child(2)')
                hp_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-hHftDr:nth-child(1) > div:nth-child(10) > div:nth-child(2)')
                attack_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(11) > div:nth-child(2)')
                crit_rate_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(12) > div:nth-child(2)')
                crit_dmge_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(13) > div:nth-child(2)')
                armor_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(14) > div:nth-child(2)')
                block_prof_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(15) > div:nth-child(2)')
                energy_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(16) > div:nth-child(2)')
                physical_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(17) > div:nth-child(2)')
                crit_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(18) > div:nth-child(2)')
                sig_info_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-eGCarw:nth-child(2) > div:nth-child(1)')
                champsjson = {
                    "name" : name_acc.text,
                    "prestige" : prestige_access.text,
                    "hp" : hp_access.text,
                    "attack" : attack_access.text,
                    "crit_rate" : crit_rate_access.text,
                    "crit_dmge" : crit_dmge_access.text,
                    "armor" : armor_access.text,
                    "block_prof" : block_prof_access.text,
                    "energy_resist" : energy_resist_access.text,
                    "physical_resist" : physical_resist_access.text,
                    "crit_resist" : crit_resist_access.text,
                    "sig_info" : sig_info_access.text,
                    "url_page" : url,
                    "champid" : f"{champname}+{tier_str}",
                    "img_potrait" : link_acc
                }
                
                db.insert_one(champsjson)
                self.name = name_acc.text
                self.prestige = prestige_access.text
                self.hp = hp_access.text
                self.attack = attack_access.text
                self.crit_rate = crit_rate_access.text
                self.crit_dmge = crit_dmge_access.text
                self.armor = armor_access.text
                self.block_prof = block_prof_access.text
                self.energy_resist = energy_resist_access.text
                self.physical_resist = physical_resist_access.text
                self.crit_resist = crit_resist_access.text
                self.sig_info = sig_info_access.text
                self.url_page = url
                self.link = link_acc
                self.champid = "Please Refresh!"
                self.img_potrait = link_acc
                browser.stop_client()
                browser.close()
                browser.quit()
            except NoSuchElementException:
                raise NoSuchElementException
        else:     
            prevx = db.find_one({"champid":info})
            self.name = prevx['name']
            self.prestige = prevx['prestige']
            self.hp = prevx['hp']
            self.attack = prevx['attack']
            self.crit_rate = prevx['crit_rate']
            self.crit_dmge = prevx['crit_dmge']
            self.armor = prevx['armor']
            self.block_prof = prevx['block_prof']
            self.energy_resist = prevx['energy_resist']
            self.physical_resist = prevx['physical_resist']
            self.crit_resist = prevx['crit_resist']
            self.sig_info = prevx['sig_info']
            self.url_page = prevx['url_page']
            self.champid = prevx['champid']
            self.link = prevx['img_potrait']   

class NewChampsDB:
    '''
    Class for getting Champs Info with ranks
    '''
    def __init__(self):
        self.champid = None         
        self.error = None
        self.url_page = None
        self.img_potrait = None                  
        self.name = None
        self.tier = None
        self.rank = None
        self.prestige = None
        self.hp = None
        self.attack = None
        self.crit_rate = None
        self.crit_dmge = None
        self.armor = None
        self.block_prof = None
        self.energy_resist = None
        self.physical_resist = None
        self.crit_resist = None
        self.sig_info = None

    def get_data(self, champid:str, tier:int, rank:int):
        if tier>6:
            self.error = 'Tier should not be above than 6'
            raise KeyError
        elif tier == 6 and rank >4:
            self.error = 'Rank of a 6 star should not be above than 4.'
            raise KeyError
        elif tier == 5 and rank>5: 
            self.error = 'Rank of a 5 star should not be above than 5.'  
            raise KeyError
        elif tier == 4 and rank>4:
            self.error = 'Rank of a 4 star should not be above than 5.'   
            raise KeyError
        elif tier == 3 and rank>4:
            self.error = 'Rank of a 3 star should not be above than 4.' 
            raise KeyError
        elif tier == 2 and rank>3: 
            self.error = 'Rank of a 2 star should not be above than 3.' 
            raise KeyError
        elif tier == 1:
            self.error = '1 star champs are not supported.'        
            raise KeyError
        else:    
            try:
                champid = champurl_getter(champid)
                with open(f'../files/{champid}.json', 'r') as f: 
                    data = json.load(f)  
                try:     
                    champ_dict = data['data'][f'{tier}+{rank}']  
                    self.champid = data['data'][f'{tier}+{rank}']['champid']  
                    self.url_page = champ_dict['url_page']
                    self.img_potrait = champ_dict['img_potrait']
                    self.name = champ_dict['name']
                    self.tier = tier
                    self.rank = champ_dict['rank']
                    self.prestige = int(champ_dict['prestige'])
                    self.hp = int(champ_dict['hp'])
                    self.attack = int(champ_dict['attack'])
                    self.crit_rate = int(champ_dict['crit_rate'])
                    self.crit_dmge = int(champ_dict['crit_dmge'])
                    self.armor = int(champ_dict['armor'])
                    self.block_prof = int(champ_dict['block_prof'])
                    self.energy_resist = int(champ_dict['energy_resist'])
                    self.physical_resist = int(champ_dict['physical_resist'])
                    self.crit_resist = int(champ_dict['crit_resist'])
                    self.sig_info = champ_dict['sig_info']
                except KeyError:
                    self.error = f'{champid} doesnt support tier {tier} of rank {rank}'   
                    raise KeyError
            except FileNotFoundError:
                self.error = f'Data with the champid: {champid} doesn\'t exist in the API Database!'
                raise FileNotFoundError
