'''
Whenever a champ gets buffed, Running this code will update the Database entry if there is one.
'''

import requests
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By

load_dotenv()

cluster_code = os.environ.get('cluster')
cluster = MongoClient(cluster_code)
db = cluster["MCOC"]["ChampsInfo"]  

champname = input('Input champcode- ')
tier_str = int(input('Input tier- '))
info = f'{champname}+{tier_str}'

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
    hp_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(10) > div:nth-child(2)')
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
    passer = True
except Exception as e:
    passer = False
    print(f'Entered champname or tier is wrong. More details ahead-\n{e}')

if passer == True:
    dbdata = db.find_one({"champid":info})
   
    if dbdata is not None:
        del dbdata['_id']
        try:
            if dbdata != champsjson:
                print('Data is different so updating...')
                db.find_one_and_replace({'champid':info}, champsjson)
                print('Successfully updated.')
            elif dbdata == champsjson:
                print('Data is same so couldn\'t update.')
        except Exception as e:
            print(f'An error occured-\n{e}')         
    else:
        print('Couldn\'t find data in the Database.')
        confirmation = input('Want me add the data? Y/N ')
        if confirmation == 'Y' or 'y':
            print(champsjson)
            confirmation2 = input('Confirm this data Y/N ')
            if confirmation2 == 'Y' or 'y':
                db.insert_one(champsjson)
                print('Successfully added')
            else:
                print('OK, That\'s a No')
        else:
            print('OK, That\'s a No')               
