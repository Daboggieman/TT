import json
# import os
from pathlib import Path
from main import (
    COUNTER_FILE, DATA_FILE
)


def load_json(file):
    with open(file, "r") as opened_file:
        loaded_file = json.load(opened_file)
    return loaded_file

def dump_json(file, data):
    try:
        with open(file, "w") as w_file:
            data = json.dump(data, w_file, indent=4)
    except (FileNotFoundError):
        print("error: file not found")
    except json.JSONDecodeError:
        print("Error: json file is broken, please review and try again")
    except PermissionError:
        print(f"Error: u do not have permission to edit file at{file}")
    else:
        print("file written successfully")


#loads counter file
if DATA_FILE.exists():
    load_json(DATA_FILE)
elif not DATA_FILE.exists():
    DATA_FILE.write_text("[]")
else:
    print(f"error finding or creating {DATA_FILE}")
    exit()


#loads counter for id generation

if COUNTER_FILE.exists():
    load_json(COUNTER_FILE)
elif not COUNTER_FILE.exists():
    COUNTER_FILE.write_text("[]")
else:
    print(f"error finding or creating {COUNTER_FILE}")
    exit()