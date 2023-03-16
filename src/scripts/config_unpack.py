import json

#unpack .json configs
def config_unpack(config_path):
    with open(config_path, "r") as file:
        return json.load(file)
