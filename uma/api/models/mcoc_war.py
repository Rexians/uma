import json

class War:

    tiers = {'Expert':{1,2}, 
             'Challenger':{3,4,5}, 
             'Hard':{6,7,8,9}, 
             'Intermediate':{10,11,12}, 
             'Normal':{13,14,15}, 
             'Easy': {16,17,18,19,20,21,22}}

    def __init__(self):
        self.season = None
        self.start = None
        self.nodes = None
        self.difficulty = None
        self.bans = None

        self.tier = None
        self.tier_multiplier = None
        self.tier_rank = None
        self.error = None

    def get_war_data(self):
        with open('./files/war_info/war_info.json', 'r') as file:
            war_data = json.load(file)["data"]
        self.season = war_data["season"]
        self.start = war_data["start"]
        self.nodes = war_data[self.difficulty]["nodes"]
        self.bans = war_data[self.difficulty]["bans"]

    def read_tier(self, tier):

        """
        Read information about war with specific tier
        """
        found = False
        try:
            for key, value in War.tiers.items():
                if int(tier) in value:
                    self.difficulty = key
                    found = True
                    break
        except ValueError as e:
            self.error = f'Incorrect type for parameter (tier). Should be integer'
            return
        if not found:
            self.error = f'Tier {tier} not found in the file'
        else:
            try:
                with open('./files/war_info/tier_info.json', 'r') as file:
                    tier_data = json.load(file)
                tier_data = tier_data['data'][str(tier)]
                self.tier = int(tier)
                self.tier_multiplier = tier_data['tier_multiplier']
                self.tier_rank = tier_data['tier_rank']

                self.get_war_data()

            except FileNotFoundError:
                self.error = f"File not found. Please report the bug"
