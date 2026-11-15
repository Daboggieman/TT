from dataclasses import dataclass, field
from typing import List
from read_load import (
    load_json, 
    COUNTER_FILE,
    DATA_FILE,
    dump_json
)

@dataclass(frozen=False)
class Task:
    id: int
    title: str = "Task"
    done: bool = False
    tags: List[str] = field(default_factory = List)


tasks = {}

def load_counter():
    if not COUNTER_FILE.exists():
        return 0
    data = load_json(COUNTER_FILE)
    if (
        not isinstance(data, int)
        or isinstance(data, bool)
        or data < 0
    ):
        raise ValueError("The counter must be a non-negative integer.")
    return data

def save_counter(counter):
    if (
        not isinstance(counter, int)
        or isinstance(counter, bool)
        or counter < 0
    ):
        raise ValueError("The counter must be a non-negative integer.")

    dump_json(COUNTER_FILE, counter)


def generate_task_id(counter):
    new_counter = counter + 1
    save_counter(new_counter)
    return new_counter, new_counter

counter = load_counter()


def add_task():
    global counter
    while True:
        title = input("enter title").strip()
        if title:
            break
        print("title cannot be empty")
    while True:
        answer = input("has this task already been completed? [y/n]").strip().lower()
        if not answer:
            print("task status cannot be empty")
            continue
        if answer not in ("y", "n"):
            print()
            continue
        if answer == "y":
            done = True
        elif answer == "n":
            done = False
            break
    while True:
        tags = list(input("[optional] add a tag for your task"))
        break
    
    task_id, counter = generate_task_id(counter)
    task = Task(
        id = task_id,
        title = title,
        done = done,
        tags = tags,
    )
    tasks[task_id] = task
    dump_json(DATA_FILE, task)
    print(f"task added: {task_id} - {task.title}")


def list_task():
    if not tasks:
        print("no task available yet")
        return
    for task in tasks.values():
        print(task.id, task.title, task.done, task.tags)
    task_id = input("enter task id").strip()
    if int(task_id) not in tasks:
        print("task not found")
        return
    task = tasks[task_id]
    print(f"id: {task.id}")
    print(f"title: {task.title}")
    print(f"id: {task.done}")
    print(f"id: {task.tags}")

    print("------------end-----------")




def complete_task(id):
    pass

def delete_task(id):
    pass

def search_by(filter):
    pass

def pending_tasks():
    pass