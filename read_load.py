import json
# import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)   # creates the folder if missing, no error if it exists
DATA_FILE = DATA_DIR / "tasks.json"

def load_json():
    with open(DATA_FILE, "r") as opened_file:
        loaded_file = json.load(opened_file)
    return loaded_file

def dump_json(filepath, data):
    try:
        with open(filepath, "w") as read_file:
            data = json.dump(data, read_file, indent=4)
    except (FileNotFoundError):
        print("error: file not found")
    except json.JSONDecodeError:
        print("Error: json file is broken, please review and try again")
    except PermissionError:
        print(f"Error: u do not have permission to edit file at{filepath}")
    else:
        print("file written successfully")