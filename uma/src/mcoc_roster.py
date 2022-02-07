from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Roster():
    def __init__(self) -> None:
        self.gamename = None
        self.error = None
        self.roster_dict = None

    def create_roster(self, gamename):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["Roster"]  
        x = db.find_one({"game_name":gamename})   
        if x is None:
            player_info = {
                'game_name':gamename,
                'discord': 'None',
                'roster': []
            }     
            db.insert_one(player_info)
            self.error = 'None'
        else:
            self.error = 'Player with this name already exists.'

    def get_roster(self, gamename):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["Roster"]  
        x = db.find_one({"game_name":gamename}, {'_id': 0})   
        if x is not None:
            self.roster_dict = x     
            self.error = 'None'
        else:
            self.error = 'Player with this name doesn\'t exists.'  

    def add_champ(self, gamename, champname, tier, signature):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["Roster"]  
        infodb = cluster['MCOC']['ChampsInfo']
        x = db.find_one({"game_name":gamename, 'champid':champname+tier}, {'_id': 0}) 
        y = infodb.find_one({'champid':f'{champname}+{tier}'})  
        if x is not None:
            if y is not None:
                if tier == 6 and signature >= 200:
                    self.error = 'Signature for a 6 star should not be above than 200'
                elif tier == 5 and signature >=200: 
                    self.error = 'Signature for a 5 star should not be above than 200'  
                elif tier == 4 and signature >=99:
                    self.error = 'Signature for a 4 star should not be above than 99'   
                elif tier == 3 and signature >=99:
                    self.error = 'Signature for a 3 star should not be above than 9' 
                elif tier == 2 or tier == 1:
                    self.error = '2 star and 1 star champs are not supported.'
                else:                                             
                    champ_info = {
                        'champ_name':y['name'],
                        'tier': tier,
                        'prestige':y['prestige'],
                        'sig_number':signature,
                        'img_link':y['img_potrait'],
                        'champid':y['champid'],
                        'url_page':y['url_page']
                    }
                    x['roster'].append(champ_info)
                    db.find_one_and_replace({"game_name":gamename}, x)
                    self.error = 'None'
            else:
                self.error = 'Champname is incorrect. Refer to https://github.com/Rexians/uma/blob/master/champnames.md for correct champnames.'    
        else:
            self.error = 'Player with this name doesn\'t exists.'                                  

    def bulk_add(self, gamename, roster_dict):
        for x in roster_dict:
            if x['tier'] >=7:
                x['tier'] = 6        
            cluster_code = os.environ.get('cluster')
            cluster = MongoClient(cluster_code)
            db = cluster["MCOC"]["Roster"]  
            infodb = cluster['MCOC']['ChampsInfo']  
            player_check = db.find_one({"game_name":gamename})
            z = db.find_one({"game_name":gamename, 'champid':f'{x["champname"]}+{x["tier"]}'}, {'_id': 0})           
            y = infodb.find_one({'champid':f'{x["champname"]}+{x["tier"]}'})  

            if player_check is not None:
                if z is None:                 
                    if y is not None:
                        if x['tier'] >=7:
                            self.error = 'Tier can\'t be greater than 7'
                        if x['tier'] == 6 and x['signature'] >= 200:
                            self.error = 'Signature for a 6 star should not be above than 200'
                        elif x['tier'] == 5 and x['signature'] >=200: 
                            self.error = 'Signature for a 5 star should not be above than 200'  
                        elif x['tier'] == 4 and x['signature'] >=99:
                            self.error = 'Signature for a 4 star should not be above than 99'   
                        elif x['tier'] == 3 and x['signature'] >=99:
                            self.error = 'Signature for a 3 star should not be above than 9' 
                        elif x['tier'] == 2 or x['tier'] == 1:
                            self.error = '2 star and 1 star champs are not supported.'       
                        else:                     
                            champ_info = {
                                'champ_name':x['champname'],
                                'tier': x['tier'],
                                'prestige': y['prestige'],
                                'sig_number':x['signature'],
                                'img_link':y['img_potrait'],
                                'champid':y['champid'],
                                'url_page':y['url_page']                
                            }
                            player_check['roster'].append(champ_info)
                            db.find_one_and_replace({"game_name":gamename}, player_check)
                            self.error = 'None'
                    else:
                        self.error = f'Entered champname- \'{x["champname"]}\' is incorrect.'   
                else:             
                    self.error = f'\'{x["champname"]}+{x["tier"]}\' already exists in your roster.'  
            else:
                self.error = 'Player with this name doesn\'t exist.'                    
