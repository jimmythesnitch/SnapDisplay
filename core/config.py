import json


class Config:
    def __init__(self, filename="config.json"):
        with open(filename, "r") as f:
            self.data = json.load(f)

    def get(self, key, default=None):
        keys = key.split(".")
        value = self.data

        for k in keys:
            if k not in value:
                return default
            value = value[k]

        return value
