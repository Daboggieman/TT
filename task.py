import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DATA_FILE = DATA_DIR / "tasks.json"
COUNTER_FILE = DATA_DIR / "counter.json"


class AlreadyCompletedError(Exception):
    pass


class CorruptedTaskError(Exception):
    pass


class IdNotFoundError(Exception):
    pass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    tags: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            done=data.get("done", False),
            tags=data.get("tags", [])
        )


def load_json(file):
    with open(file, "r") as opened_file:
        if not opened_file.read().strip():
            return {}

        opened_file.seek(0)
        return json.load(opened_file)


def dump_json(file, data):
    try:
        if isinstance(data, Task):
            data = data.to_dict()

        elif isinstance(data, dict):
            data = {
                key: value.to_dict() if isinstance(value, Task) else value
                for key, value in data.items()
            }

        with open(file, "w") as w_file:
            json.dump(data, w_file, indent=4)

    except (FileNotFoundError, PermissionError, TypeError, OSError) as e:
        print(f"Error saving JSON: {e}")
        return False

    else:
        return True


def load_counter():
    if not COUNTER_FILE.exists():
        dump_json(COUNTER_FILE, 0)
        return 0

    if COUNTER_FILE.stat().st_size == 0:
        dump_json(COUNTER_FILE, 0)
        return 0

    data = load_json(COUNTER_FILE)

    if (
        isinstance(data, bool)
        or not isinstance(data, int)
        or data < 0
    ):
        raise ValueError("The counter must be a non-negative integer.")

    return data


def save_counter(counter):
    if (
        isinstance(counter, bool)
        or not isinstance(counter, int)
        or counter < 0
    ):
        raise ValueError("The counter must be a non-negative integer.")

    return dump_json(COUNTER_FILE, counter)


def generate_task_id(counter):
    new_counter = counter + 1

    if not save_counter(new_counter):
        raise OSError("Unable to save the task counter.")

    return new_counter, new_counter


def load_tasks():
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return {}

    data = load_json(DATA_FILE)

    if not isinstance(data, dict):
        raise ValueError("Invalid tasks file format.")

    loaded_tasks = {}

    for key, value in data.items():
        if not isinstance(value, dict):
            raise ValueError(f"Invalid task data for ID {key}.")

        task = Task.from_dict(value)
        loaded_tasks[int(key)] = task

    return loaded_tasks


counter = load_counter()
tasks = load_tasks()


def add_task():
    global counter

    while True:
        title = input("Enter title:\n").strip()

        if title:
            break

        print("Title cannot be empty.")

    while True:
        answer = input(
            "Has this task already been completed? [y/n]: "
        ).strip().lower()

        if answer not in ("y", "n"):
            print("Please enter 'y' or 'n'.")
            continue

        done = answer == "y"
        break

    tags = [
        tag.strip()
        for tag in input(
            "[Optional] Add tags (separate with commas):\n"
        ).split(",")
        if tag.strip()
    ]

    task_id, new_counter = generate_task_id(counter)

    task = Task(
        id=task_id,
        title=title,
        done=done,
        tags=tags
    )

    tasks[task_id] = task

    if not dump_json(DATA_FILE, tasks):
        del tasks[task_id]
        print("Task could not be saved.")
        return

    counter = new_counter

    print(f"Task added: {task_id} - {task.title}")


def list_task():
    if not tasks:
        print("No tasks available yet.")
        return

    for task in tasks.values():
        print(
            f"ID: {task.id} | "
            f"Title: {task.title} | "
            f"Status: {'Completed' if task.done else 'Pending'} | "
            f"Tags: {task.tags}"
        )

    print("-----------------------------------")

    task_id = input("Enter task ID: ").strip()

    try:
        task_id = int(task_id)
    except ValueError:
        print("Invalid task ID.")
        return

    task = tasks.get(task_id)

    if task is None:
        print("Task not found.")
        return

    print("\n---------- TASK  ----------")
    print(f"ID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Status: {'Completed' if task.done else 'Pending'}")
    print(f"Tags: {task.tags}")
    print("-----------------------------------")


def complete_task(id):
    task = tasks.get(id)

    if task is None:
        raise IdNotFoundError(
            "ID not found: please input a valid ID."
        )

    if not isinstance(task.done, bool):
        raise CorruptedTaskError(
            "This task has been corrupted. Please review it."
        )

    if task.done:
        raise AlreadyCompletedError(
            "This task has already been completed."
        )

    task.done = True

    if not dump_json(DATA_FILE, tasks):
        task.done = False
        print("Unable to save task changes.")
        return

    print("------------- Task completed -------------")


def delete_task(id):
    task = tasks.get(id)

    if task is None:
        raise IdNotFoundError(
            "ID not found: please input a valid ID."
        )

    del tasks[id]

    if not dump_json(DATA_FILE, tasks):
        tasks[id] = task
        print("Unable to save task changes.")
        return

    print("-------------- Task Deleted --------------")


def search_by(filter):
    results = []

    for task in tasks.values():
        if filter.lower() in task.title.lower():
            results.append(task)

    return results


def pending_tasks():
    pending = [
        task for task in tasks.values()
        if not task.done
    ]

    if not pending:
        print("No pending tasks available.")
        return

    for task in pending:
        print(
            f"ID: {task.id} | "
            f"Title: {task.title} | "
            f"Tags: {task.tags}"
        )

    print("-----------------------------------")

    task_id = input("Enter task ID: ").strip()

    try:
        task_id = int(task_id)
    except ValueError:
        print("Invalid ID: please enter a numeric ID.")
        return

    task = tasks.get(task_id)

    if task is None:
        print("Task not found.")
        return

    if task.done:
        print("This task has already been completed.")
        return

    print("\n---------- TASK DETAILS ----------")
    print(f"ID: {task.id}")
    print(f"Title: {task.title}")
    print("Status: Pending")
    print(f"Tags: {task.tags}")
    print("-----------------------------------")