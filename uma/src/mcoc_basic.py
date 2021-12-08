from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

class Champs:
    '''
    The Deprecated Method to get Info
    '''
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

    def champs_info(self, champname:str, tier_str:int):
        url = f"https://auntm.ai/champions/{champname}/tier/{tier_str}"
        opts = webdriver.ChromeOptions()
        opts.add_argument("--no-sandbox");
        opts.add_argument("--disable-dev-shm-usage");
        opts.add_argument(" --headless");
        opts.add_argument("--disable-gpu")        
        browser = webdriver.Chrome(chrome_options=opts)
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
        sig_info_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-gsxnyZ:nth-child(2) > div:nth-child(1)')
        
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
        browser.quit()