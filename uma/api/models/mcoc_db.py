import json
from ..helpers.champurl import champurl_getter

class NewChampsDB:
    '''
    Class for getting Champs Info with ranks
    '''
    def __init__(self):
        self.champid = None         
        self.error = None
        self.url_page = None
        self.img_portrait = None                  
        self.name = None
        self.class_type = None
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
        self.challenger_rating = None
        self.contact = None
        self.tags = None
        self.released = None
        self.est_release = None

    def get_data(self, champid:str, tier:int, rank:int):
        if tier>6:
            self.error = 'Tier should not be above 6'
            raise KeyError
        elif tier == 6 and rank >4:
            self.error = 'Rank of a 6 star should not be above 4.'
            raise KeyError
        elif tier == 5 and rank>5: 
            self.error = 'Rank of a 5 star should not be above 5.'  
            raise KeyError
        elif tier == 4 and rank>5:
            self.error = 'Rank of a 4 star should not be above 5.'   
            raise KeyError
        elif tier == 3 and rank>4:
            self.error = 'Rank of a 3 star should not be above 4.' 
            raise KeyError
        elif tier == 2 and rank>3: 
            self.error = 'Rank of a 2 star should not be above 3.' 
            raise KeyError
        elif tier == 1 and rank>2:
            self.error = 'Rank of a 1 star should not be above 3.'        
            raise KeyError
        if tier<0:
            self.error = 'Tier should not be below 0'
            raise KeyError
        else:    
            try:
                champid = champurl_getter(champid)
                with open(f'./files/champ_stats/{champid}.json', 'r') as f: 
                    data = json.load(f)  
                try:
                    champ_dict = data['data'][f'{tier}+{rank}']  

                    self.released = data.get('released', None)                    
                    self.champid = data['data'][f'{tier}+{rank}']['champid']  
                    self.url_page = champ_dict['url_page']
                    self.img_portrait = data['img_portrait']
                    self.name = data['name']
                    self.tier = tier
                    self.class_type = data['class']
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
                    self.challenger_rating = champ_dict['challenger_rating']
                    self.contact = data['contact']
                    self.tags = data['tags']
                except KeyError:
                    self.error = f'{champid} doesnt support tier {tier} of rank {rank}'   
                    raise KeyError
            except FileNotFoundError:
                self.error = f'Data with the champid: {champid} doesn\'t exist in the API Database!'
                raise FileNotFoundError
