import json

def read_test_data(path):
    with open(path) as f:
        return json.load(f)