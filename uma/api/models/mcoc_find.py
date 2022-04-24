import json
from ..helpers.champurl import champurl_getter


class Finder:
    """
    Class for getting Champs Info with ranks
    """

    def __init__(self):
        self.champid = None
        self.error = None
        self.url_page = None
        self.img_portrait = None
        self.name = None
        self.class_type = None
        self.find = None

    def get_data(self, champid: str):
        try:
            champid = champurl_getter(champid)
            with open(f"./files/champ_stats/{champid}.json", "r") as f:
                data = json.load(f)
            champ_dict = data["data"]

            self.champid = data["data"]["2+1"]["champid"]
            self.url_page = champ_dict["2+1"]["url_page"]
            self.img_portrait = data["img_portrait"]
            self.name = data["name"]
            self.class_type = data["class"]
            self.find = champ_dict["find"]
        except FileNotFoundError:
            self.error = (
                f"Data with the champid: {champid} doesn't exist in the API Database!"
            )
            raise FileNotFoundError
