# this interacts with the user, this is the main orchestrator of the application
from pathlib import Path
import sys
from task import (
    add_task,
    complete_task,
    delete_task,
    list_task,
    pending_tasks,
    load_counter,
    load_json,
    search_by
)

counter = load_counter() # move this into the main.py file, tasks should contain the functions, and not call them 

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)   # creates the folder if missing, no error if it exists
DATA_FILE = DATA_DIR / "tasks.json"
COUNTER_FILE = DATA_DIR / "counter.json"

tasks = load_json(DATA_FILE)

print("-----------Tasks Tracker----------")
print("choose an action")
print("1. add task")
print("2. complete task")
print("3. list tasks")
print("4. delete task")
print("5. pending tasks")
print("6. search task")
print("7. Exit")
print("----------------------------------")
print("\n")

user_action = int(input("select an action: "))

match user_action:
    case 1:
        add_task()
    case 2:
        complete_input_id = int(input("input the task ID: "))
        complete_task(complete_input_id)
    case 3:
        list_task()
    case 4: 
        delete_task_id = int(input("input the task ID: "))
        delete_task(delete_task_id)
    case 5:
        pending_tasks()
    case 6:
        search_filter = (input("input your keyword"))
        search_by(search_filter)
    case 7:
        print("exiting....")
        sys.exit(0)

