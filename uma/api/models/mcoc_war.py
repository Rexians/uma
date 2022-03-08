import json

class War:

    tiers = {'Expert':[1,2], 
             'Challenger':[3,4,5], 
             'Hard':[6,7,8,9], 
             'Intermediate':[10,11,12], 
             'Normal':[13,14,15], 
             'Easy': [16,17,18,19,20,21,22]}

    def __init__(self):
        self.tier = None
        self.nodes = None
        self.difficulty = None
        self.tier_multiplier = None
        self.tier_rank = None
        self.error = None


    def match_nodes(self, diff):
        """
        Convert all the ids of the nodes into their corresponding names
        """
        try:
            with open('./files/nodes/nodes.json', 'r') as file:
                nodes = json.load(file)
            nodes = nodes['data']
            with open('./files/war_info/war_info.json', 'r') as file:
                war = json.load(file)
            war = war['data'][diff]['nodes']
        except FileNotFoundError:
            self.error = f"File not found. Please report the bug"

        for key, value in war.items():
            node_names = []
            for node in value:
                node_names.append(nodes[str(node)]['node_name'])
            war[key] = node_names
        
        return war

    def read_tier(self, tier):

        """
        Read information about war with specific tier
        """
        found = False
        diff = None
        try:
            for key, value in War.tiers.items():
                if int(tier) in value:
                    diff = key
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
                nodes = self.match_nodes(diff)
                self.tier = tier
                self.nodes = nodes
                self.difficulty = diff
                self.tier_multiplier = tier_data['tier_multiplier']
                self.tier_rank = tier_data['tier_rank']    
            except FileNotFoundError:
                self.error = f"File not found. Please report the bug"
