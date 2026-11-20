import json
import os
from pathlib import Path
from tt.read_load import(
    load_json,
    dump_json
)
from tt.task import (
    Task,
    add_task,
    list_task,
    complete_task,
    delete_task,
    search_by,
    pending_tasks
)

tasks={}
task_id_counter= 0

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)   # creates the folder if missing, no error if it exists
DATA_FILE = DATA_DIR / "tasks.json"
COUNTER_FILE = DATA_DIR / "counter.json"

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


# filepath = os.getcwd() + "/tasks.json"
