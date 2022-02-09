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

    def create_roster(self, gamename):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["Account"]  
        x = db.find_one({"game_name":gamename})   
        if x is None:
            player_info = {
                'game_name':gamename,
                'discord_id': 'None',
                'roster': []
            }     
            db.insert_one(player_info)
            self.error = ''
        else:
            self.error = 'Player with this name already exists.'

    def get_roster(self, gamename):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        db = cluster["MCOC"]["Roster"]  
        x = db.find_one({"game_name":gamename}, {'_id': 0})   
        if x is not None:
            self.roster_dict = x     
            self.error = ''
        else:
            self.error = 'Player with this name doesn\'t exists.'  

    def add_champ(self, gamename, champname, tier, signature):
        cluster_code = os.environ.get('cluster')
        cluster = MongoClient(cluster_code)
        rosterdb = cluster["MCOC"]["Account"]  
        infodb = cluster['MCOC']['ChampsInfo']
        player_check = rosterdb.find_one({"game_name":gamename}, {'_id': 0}) 
        champ_details = infodb.find_one({'champid':f'{champname}+{tier}'})
        create_new = True  
        for roster_dict in player_check['roster']:
            if roster_dict['champ_name'] == champ_details['name'] and roster_dict['tier'] == int(tier):
                create_new = False
            break
        if player_check is not None:
            if champ_details is not None:
                if create_new == True:
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
                            'champ_name':champ_details['name'],
                            'tier': tier,
                            'prestige':champ_details['prestige'],
                            'sig_number':signature,
                            'img_link':champ_details['img_potrait'],
                            'champid':f'{champ_details["champid"]}+{signature}',
                            'url_page':champ_details['url_page']
                        }
                        player_check['roster'].append(champ_info)
                        rosterdb.find_one_and_replace({"game_name":gamename}, player_check)
                        self.details = f'Added {tier} star {champ_details["name"]} of signature {signature}'
                else:
                    #Updates the signature and champid
                    for roster_dict in player_check['roster']:
                        if roster_dict['champ_name'] == champ_details['name'] and roster_dict['tier'] == int(tier): 
                            self.details = f'Updated {tier} star {champ_details["name"]} of previous signature {roster_dict["sig_number"]} to new signature {signature}'
                            roster_dict['sig_number'] = signature
                            roster_dict['champid'] = f'{champ_details["champid"]}+{signature}'
                            
                        break        
                    rosterdb.find_one_and_replace({"game_name":gamename}, player_check)                         
            else:
                self.error = 'Champname is incorrect. Refer to https://github.com/Rexians/uma/blob/master/champnames.md for correct champnames.'    
        else:
            self.error = 'Player with this name doesn\'t exists.'                                  

#Heavily Bugged feature! Still Developing...
    def bulk_add(self, gamename, roster_dict):
        for x in roster_dict:
            if x['tier'] >=7:
                x['tier'] = 6        
            cluster_code = os.environ.get('cluster')
            cluster = MongoClient(cluster_code)
            db = cluster["MCOC"]["Roster"]  
            infodb = cluster['MCOC']['ChampsInfo']  
            player_check = db.find_one({"game_name":gamename})
            #champ_check = db.find_one({"game_name":gamename, 'champid':f'{x["champname"]}+{x["tier"]}+{x["signature"]}'})#, {'_id': 0}           
            correct_check = infodb.find_one({'champid':f'{x["champname"]}+{x["tier"]}'})  

            if player_check is not None:
                champ_check = player_check['roster']
                champ_found = False
                for champs in champ_check:
                    if champs['champid'] == f'{x["champname"]}+{x["tier"]}+{x["signature"]}':
                        champ_found = True
                        break
                    else:    
                        continue
                if champ_found is False:               
                    if correct_check is not None:
                        if x['tier'] >=7:
                            self.error = self.error+f'{x["champname"]}+{x["tier"]}- Tier can\'t be greater than 6\n'
                        if x['tier'] == 6 and x['signature'] > 200:
                            self.error = self.error+f'{x["champname"]}+{x["tier"]}+{x["signature"]}- Signature for a 6 star should not be above than 200\n'
                        elif x['tier'] == 5 and x['signature'] >200: 
                            self.error = self.error+f'{x["champname"]}+{x["tier"]}+{x["signature"]}- Signature for a 5 star should not be above than 200\n'  
                        elif x['tier'] == 4 and x['signature'] >99:
                            self.error = self.error+f'{x["champname"]}+{x["tier"]}+{x["signature"]}- Signature for a 4 star should not be above than 99\n'   
                        elif x['tier'] == 3 and x['signature'] >99:
                            self.error = self.error+f'{x["champname"]}+{x["tier"]}+{x["signature"]}- Signature for a 3 star should not be above than 99\n' 
                        elif x['tier'] == 2 or x['tier'] == 1:
                            self.details = self.details+f'{x["champname"]}+{x["tier"]}+{x["signature"]}- 2 star and 1 star champs are not supported.\n'       
                        else:                     
                            champ_info = {
                                'champ_name':x['champname'],
                                'tier': x['tier'],
                                'prestige': correct_check['prestige'],
                                'sig_number':x['signature'],
                                'img_link':correct_check['img_potrait'],
                                'champid':f"{correct_check['champid']}+{x['signature']}",
                                'url_page':correct_check['url_page']                
                            }
                            player_check['roster'].append(champ_info)
                            db.find_one_and_replace({"game_name":gamename}, player_check)
                            self.error = self.error+f'{x["champname"]}+{x["tier"]}+{x["signature"]}- Added\n'
                    else:
                        self.error = self.error+f'Entered champname- \'{x["champname"]}\' is incorrect.\n'   
                else:             
                    self.error = self.error+f'\'{x["champname"]}+{x["tier"]}+{x["signature"]}\' already exists in your roster.\n'  
            else:
                self.error = 'Player with this name doesn\'t exist.'                    
