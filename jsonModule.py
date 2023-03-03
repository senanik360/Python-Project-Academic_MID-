import json

jsonFileName='E:\\Python\\MID Project\\PcList.json'


def load():
    with open(jsonFileName) as f:
            FileContent=json.load(f) 
    return FileContent