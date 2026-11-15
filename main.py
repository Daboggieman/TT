import json
import os
from pathlib import Path
from read_load import(
    load_json,
    dump_json
)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)   # creates the folder if missing, no error if it exists
DATA_FILE = DATA_DIR / "tasks.json"

if DATA_FILE.exists():
    load_json()
elif not DATA_FILE.exists():
    DATA_FILE.write_text("[]")
else:
    print(f"error finding or creating {DATA_FILE}")
    exit()
# filepath = os.getcwd() + "/tasks.json"


all_tasks = load_json()