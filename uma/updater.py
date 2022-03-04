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
            self.champsjson = {
                "name" : name_acc.text,
                "rank" : rank,
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
                "champid" : f"{champname}+{tier}+{rank}",
                "img_potrait" : link_acc
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
            champ_json[f"{tier}+{rank}"]= champs.champsjson
            print(f'Scraped {tier}* {champ} of rank {rank}')                      
        except LookupError:
            print(f'Got A Error from {tier}* {champ} of {rank}.\nDocument in DB will be created but data will have to be entered manually.')    
            error_list.append(f'{tier}* {champ}, Rank {rank}')

champ_json = {'champid':champ_json_name, 'data':champ_json}
db.insert_one(champ_json)    
try:
    champ_json.pop('_id')
except:
    pass    
with open(f'./uma/files/champ_stats/{champ_json_name}.json', 'w') as f:
    json.dump(champ_json, f)      

print('DATA ADDED')
if len(error_list) == 0:
    print('No Errors came :D #Winning!')
else:
    print('At last, the errors that came were-')
    print(error_list)
