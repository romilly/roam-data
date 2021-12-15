import json


def import_json(filename):
    with open(filename) as f:
        return json.load(f)