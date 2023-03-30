import json

class Battlegrounds:

    def __init__(self):
        self.start = None
        self.end = None
        self.season = None
        self.victory_track = None
        self.victory_track_nodes = None
        self.gladiator_circuit = None
        self.gladiator_circuit_nodes = None
        self.error = None

    def get_tracks(self):
        with open(f"./files/battlegrounds/tracks.json", "r") as f:
            data = json.load(f)['data']
        return data

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

            tracks = self.get_tracks()

            self.start = data['start']
            self.end = data['end']
            self.season = data['season']
            self.victory_track = tracks['victory_track']
            self.victory_track_nodes = data['victory_track_nodes']
            self.gladiator_circuit = tracks['gladiator_circuit']
            self.gladiator_circuit_nodes = data['gladiator_circuit_nodes']
        except FileNotFoundError:
            self.error = f"File not found. Please report the bug"