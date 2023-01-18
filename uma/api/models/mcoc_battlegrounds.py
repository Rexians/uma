import json

class Battlegrounds:

    def __init__(self):
        self.start = None
        self.end = None
        self.season = None
        self.victory_track = None
        self.gladiator_circuit = None
        self.error = None

    def read_battleground_data(self, season: int):

        try:
            season = int(season)
        except ValueError:
            self.error = f'Incorrect type for parameter (season). Should be integer'
            return

        if (season < 4):
            self.error = "Season below 4 not available."
            return

        try:
            season = int(season)
            with open(f"./files/battlegrounds/battlegrounds_season_{season}.json", "r") as f:
                data = json.load(f)['data']

            self.start = data['start']
            self.end = data['end']
            self.season = data['season']
            self.victory_track = data['victory_track']
            self.gladiator_circuit = data['gladiator_circuit']
        except FileNotFoundError:
            self.error = f"File not found. Please report the bug"