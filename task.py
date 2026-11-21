# holds all the necessary files to parse to the main.py file
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List
from main import (
    COUNTER_FILE,
    DATA_FILE
)

tasks = {}


class AlreadyCompletedError(Exception):
    pass

class CorruptedTaskError(Exception):
    pass

class IdNotFoundError(Exception):
    pass
@dataclass(frozen=False)
class Task:
    """dataclass: the applications data structure"""
    id: int
    title: str = "Task"
    done: bool = False
    tags: List[str] = field(default_factory = List)

def load_json(file):
    """
        this function loads json format file from whatever directory it is sent to
    """
    with open(file, "r") as opened_file:
        loaded_file = json.load(opened_file)
    return loaded_file

def dump_json(file, data):
    """
        this function dumps json format data into the specified .json file
    """
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

def load_counter():
    """
        this loads the counter file to keeps track of the current assigned id, to avoid loss of context and duplication of ID
    """
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
    """
        saves the latest newly assigned id to the counter file
    """
    if (
        not isinstance(counter, int)
        or isinstance(counter, bool)
        or counter < 0
    ):
        raise ValueError("The counter must be a non-negative integer.")

    dump_json(COUNTER_FILE, counter)

def generate_task_id(counter):
    """
        generates the task id and returns the value to send to the counter file for the "save_counter()" function to load it
    """
    new_counter = counter + 1
    save_counter(new_counter)
    return new_counter, new_counter

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


# def complete_task(id):
#     try:
#         for task in tasks.values():
#             if task.id == id:
#                 if task.done == False:
#                     task.done = True
#                 elif task.done == True:
#                     print("this task has already been completed")
#                     raise AlreadyCompletedError("this task has already been completed")
#                 else:
#                     print("this task has been corrupted, please delete and re-enter the task")
#                     raise CorruptedTaskError("this task has been corrupted, please delete and re-enter the task")
#     except:
#         print("ID not found: please input a valid Id")
#         raise IdNotFoundError("ID not found: please input a valid Id")


def complete_task(id):
    task = tasks.get(id)

    if task is None:
        raise IdNotFoundError("ID not found: please input a valid ID")

    if not isinstance(task.done, bool):
        raise CorruptedTaskError(
            "This task has been corrupted, please delete and re-enter it"
        )

    if task.done:
        raise AlreadyCompletedError(
            "This task has already been completed"
        )

    task.done = True
    print("-------------Task completed -------------")

def delete_task(id):
    task = tasks.get(id)
    if task is None:
            raise IdNotFoundError("ID not found: please input a valid ID")
    del tasks[id]
    print("-------------- Task Deleted--------------")

    
def search_by(filter):
    results = []

    for task in tasks.values():
        if filter.lower() in task.title.lower():
            results.append(task)

    if not results:
        return []

    return results

def pending_tasks():
    pending = [task for task in tasks.values() if not task.done]

    if not pending:
        print("No pending tasks available")
        return

    for task in pending:
        print(f"ID: {task.id} | Title: {task.title} | Tags: {task.tags}")

    print("-----------------------------------")

    task_id = input("Enter task ID: ").strip()

    try:
        task_id = int(task_id)
    except ValueError:
        print("Invalid ID: please enter a numeric ID")
        return

    task = tasks.get(task_id)

    if task is None:
        print("Task not found")
        return

    if task.done:
        print("This task is not pending; it has already been completed")
        return

    print("\n---------- TASK DETAILS ----------")
    print(f"ID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Status: {'Completed' if task.done else 'Pending'}")
    print(f"Tags: {task.tags}")
    print("------------ END ------------")