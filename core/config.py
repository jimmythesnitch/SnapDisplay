import json


class Config:

    def __init__(self, filename="config.json"):

        with open(filename, "r") as f:
            self.data = json.load(f)

    def get(self, key, default=None):

        value = self.data

        for part in key.split("."):

            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default

        return value
