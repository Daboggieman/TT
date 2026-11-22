# this interacts with the user, this is the main orchestrator of the application
from pathlib import Path
from task import (
    add_task,
    complete_task,
    delete_task,
    list_task,
    pending_tasks,
    load_counter,
    save_counter,
    load_json,
    dump_json,
    Task,
    generate_task_id,
    search_by
)

counter = load_counter() # move this into the main.py file, tasks should contain the functions, and not call them 

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)   # creates the folder if missing, no error if it exists
DATA_FILE = DATA_DIR / "tasks.json"
COUNTER_FILE = DATA_DIR / "counter.json"

def main():
    pass