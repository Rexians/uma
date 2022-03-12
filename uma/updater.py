'''
Whenever a champ gets buffed, Running this code will update the Database entry if there is one.
'''
import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

load_dotenv()

cluster_code = os.environ.get('cluster')
cluster = MongoClient(cluster_code)
db = cluster["MCOC"]["Champs"]  

class ChampsInfo():
    def __init__(self) -> None:
        pass

    def get_champ_info(self, champname, tier, rank):
        url = f"https://auntm.ai/champions/{champname}/tier/{tier}"
        opts = webdriver.ChromeOptions()
        opts.add_argument("--no-sandbox");
        opts.add_argument("--disable-dev-shm-usage");
        opts.add_argument(" --headless");
        opts.add_argument("--disable-gpu")        
        browser = webdriver.Chrome(options=opts)
        try:
            browser.get(url)
            browser.maximize_window()
            
            browser.find_element(By.ID, 'rankDropdown').click()
            browser.find_element(By.XPATH, f"//*[contains(text(), 'RANK {rank}')]").click()
            
            self.name_acc = browser.find_element(By.CSS_SELECTOR, '.sc-bZSQDF')
            self.name = self.name_acc.text
            self.link_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-bkzZxe:nth-child(1) > img:nth-child(1) ').get_attribute("src")
            self.link_acc = self.link_acc.replace('https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_', 'https://mcoc.rexians.tk/assets/portraits/')
            self.prestige_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(9) > div:nth-child(2)')
            self.hp_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-hHftDr:nth-child(1) > div:nth-child(10) > div:nth-child(2)')
            self.champ_class = browser.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div/div").get_attribute('title')
            self.champ_class = self.champ_class
            self.attack_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(11) > div:nth-child(2)')
            self.crit_rate_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(12) > div:nth-child(2)')
            self.crit_dmge_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(13) > div:nth-child(2)')
            self.armor_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(14) > div:nth-child(2)')
            self.block_prof_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(15) > div:nth-child(2)')
            self.energy_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(16) > div:nth-child(2)')
            self.physical_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(17) > div:nth-child(2)')
            self.crit_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(18) > div:nth-child(2)')
            self.sig_info_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-eGCarw:nth-child(2) > div:nth-child(1)')
            self.champsjson = {
                #"name" : self.name_acc.text,
                "rank" : rank,
                "prestige" : self.prestige_access.text,
                "hp" : self.hp_access.text,
                "attack" : self.attack_access.text,
                "crit_rate" : self.crit_rate_access.text,
                "crit_dmge" : self.crit_dmge_access.text,
                "armor" : self.armor_access.text,
                "block_prof" : self.block_prof_access.text,
                "energy_resist" : self.energy_resist_access.text,
                "physical_resist" : self.physical_resist_access.text,
                "crit_resist" : self.crit_resist_access.text,
                "sig_info" : self.sig_info_access.text,
                "url_page" : url,
                "champid" : f"{champname}+{tier}+{rank}",
                #"img_potrait" : self.link_acc
            }   
            browser.close()    
        except:
            raise LookupError

champ = input('Input auntm.ai champcode- ')
champ_json_name = input('Input name for the json- ')

def get_ranks_list(tier) -> list:
    if tier == 6:
        return([1,2,3,4])
    elif tier == 5 or tier == 4:
        return([1,2,3,4,5])    
    elif tier == 3:
        return([1,2,3,4])
    elif tier == 2:
        return([1,2,3]) 

champs = ChampsInfo()

champ_json = {}
error_list = []
for tier in range(2,7):
    ranks = get_ranks_list(tier)
    for rank in ranks:
        try:
            print(f'Going for {tier}* {champ} of rank {rank}')
            champs.get_champ_info(champ, tier, rank)
            champid = champ
            champ_json[f"{tier}+{rank}"]= champs.champsjson
            print(f'Scraped {tier}* {champ} of rank {rank}')                      
        except LookupError:
            print(f'Got A Error from {tier}* {champ} of {rank}.\nDocument in DB will be created but data will have to be entered manually.')    
            error_list.append(f'{tier}* {champ}, Rank {rank}')

champ_json = {
    'champid':champ,
    'name':champs.name,
    'class':champs.champ_class,
    'img_portrait':champs.link_acc, 
    'data':champ_json
    }
db.insert_one(champ_json)    
try:
    champ_json.pop('_id')
except:
    pass    
with open(f'./uma/files/champ_stats/{champ_json_name}.json', 'w') as f:
    json.dump(champ_json, f, indent=4)      

print('DATA ADDED')
if len(error_list) == 0:
    print('No Errors came :D #Winning!')
else:
    print('At last, the errors that came were-')
    print(error_list)
