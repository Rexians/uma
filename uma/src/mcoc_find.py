from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class champs_detailed:
    '''
    Class for finding the Champs detailed information
    '''

    def __init__(self):
        self.story_quest = None
        self.event_quest = None
        self.alliance_quest = None
        self.incursions = None
        self.daily_quests = None
        self.special_quests = None
        self.back_quests = None
        self.img_potrait = None
        self.name = None
        self.url_page = None
        self.error = None


    def champs_find(self, champname:str):
        '''
        Find where a specific champion can be found
        '''
        try:
            url = f"https://auntm.ai/champions/{champname}"    
            opts = webdriver.ChromeOptions()
            opts.add_argument("--no-sandbox");
            opts.add_argument("--disable-dev-shm-usage");
            opts.add_argument("--remote-debugging-port=9222");
            opts.add_argument(" --headless");
            opts.add_argument("--disable-gpu")
            browser = webdriver.Chrome(options=opts)
            browser.get(url)        
            browser.maximize_window()
            link_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-bkzZxe:nth-child(1) > img:nth-child(1) ').get_attribute("src")
            name_acc = browser.find_element(By.CSS_SELECTOR, '.sc-bZSQDF')
            
            browser.execute_script("window.scrollBy(0,1500)","")
            try:
                story_quest_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(2) > div:nth-child(1)') 
                story_quest = story_quest_acc.text
                story_quest = story_quest.replace("\n", ", ")
                self.story_quest = story_quest
            except NoSuchElementException:
                self.story_quest = 'Couldn\'t find'
            
            try:
                event_quest_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(4)') 
                event_quest = event_quest_acc.text
                event_quest = event_quest.replace("\n", ", ")
                self.event_quest = event_quest
            except NoSuchElementException:
                self.event_quest = 'Couldn\'t find'
            
            try:
                alliance_quest_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(6) > div:nth-child(1)')
                alliance_quest = alliance_quest_acc.text
                alliance_quest = alliance_quest.replace("\n", ", ")
                self.alliance_quest = alliance_quest
            except NoSuchElementException:
                self.alliance_quest = 'Couldn\'t find'

            try:
                incursions_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(10)')
                incursions = incursions_acc.text
                incursions = incursions.replace("\n", ", ")
                self.incursions = incursions
            except NoSuchElementException:
                self.incursions = 'Couldn\'t find'
            
            try:
                daily_quests_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(10) > div:nth-child(1)')
                daily_quests = daily_quests_acc.text
                daily_quests = daily_quests.replace("\n", ", ")
                self.daily_quests = daily_quests
            except NoSuchElementException:
                self.daily_quests = 'Couldn\'t find'

            try:
                special_quests_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(12)')
                special_quests = special_quests_acc.text
                special_quests = special_quests.replace("\n", ", ")
                self.special_quests = special_quests
            except NoSuchElementException:
                self.special_quests = 'Couldn\'t find'
            
            try:
                back_quests_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-hjWSAi:nth-child(14)')
                back_quests = back_quests_acc.text
                back_quests = back_quests.replace("\n", ", ")
                self.back_quests = back_quests
            except NoSuchElementException:
                self.back_quests = 'Couldn\'t find'
            
            name_text = name_acc.text
            self.img_potrait = link_acc
            self.name = name_text
            self.url_page = url
            browser.stop_client()
            browser.close()
            browser.quit()
            self.error = {
                        "detail" : "Error on Finding Champ/Element on AUNTM.ai",
                        "status" : 404}
        except NoSuchElementException:
            raise NoSuchElementException
                

