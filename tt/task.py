from dataclasses import dataclass, field
from typing import List
from main import 
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
counter = 0

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
    new_counter, task_id = counter + 1
    task_id = f"{new_counter}"
    save_counter(new_counter)
    counter = new_counter
    return task_id


def add_task():
    while True:
        title = input("enter title").strip()
        if title:
            break
        print("title cannot be empty")
    while True:
        done = input("has this task already been completed? [y/n]").strip().lower()
        if done:
            break
        print("task cannot be empty")
        if done == "y":
            done = True
        elif done == "n":
            done = False
        
    while True:
        tags = list(input("[optional] add a tag for your task"))
        if tags:
            tags = [""]
    id = generate_task_id(counter)

def list_all_task():
    pass

def complete_task(id):
    pass

def delete_task(id):
    pass

def search_by(filter):
    pass

def pending_tasks():
    pass