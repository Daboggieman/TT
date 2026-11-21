# this interacts with the user, this is the main orchestrator of the application
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
