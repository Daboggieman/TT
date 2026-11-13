import json

filepath = "/home/recoding/TT/"

def load_json(filepath):
    with open(filepath, "r") as opened_file:
        loaded_file = json.load(opened_file)
    return loaded_file

def dump_json(filepath, data):
    try:
        with open(filepath, "w") as read_file:
            data = json.dump(data, read_file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        print("error")
    else:
        print("file written successfully")