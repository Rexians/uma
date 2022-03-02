from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Roster():
    def __init__(self) -> None:
        self.gamename = None
        self.error = ''
        self.details = ''
        self.roster_dict = None

    def get_roster(self, gamename):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["Account"]  
        x = db.find_one({"game_name":gamename}, {'_id': 0})   
        if x is not None:
            try:
                x.pop('alliance')
            except:
                pass    
            self.roster_dict = x     
            self.error = ''
        else:
            self.error = 'Player with this name doesn\'t exists.'  
