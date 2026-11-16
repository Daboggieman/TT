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




# filepath = os.getcwd() + "/tasks.json"
