import os
import json


def open_file():
    dir_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'files', 'products.json')
    with open(file_path) as f:
        file = json.load(f)
        return file