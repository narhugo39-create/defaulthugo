import yaml
import os

class Config:
    def __init__(self, path='config.yaml'):
        with open(path, 'r') as f:
            self.data = yaml.safe_load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)

config = Config()
