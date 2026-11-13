# Project: Task Tracker (CLI)

## Goal

Build a command-line task manager that stores everything in a JSON file, so tasks survive after the script closes.

## Data model

A `Task` dataclass with these fields:

- `id` (int)
- `title` (str)
- `done` (bool, defaults to `False`)
- `tags` (list of str, defaults to an empty list)

## Restrictions

- Only what we've covered: dataclasses, `field(default_factory=...)`, `asdict`, `Task(**d)`, `json`, `os.path.exists`, list comprehensions, `sorted`, `next(...)`, `input()`, and `while` loops
- No dicts as your main data structure. Tasks live as `Task` objects in a list, and dicts only appear briefly during save/load
- No third-party libraries
- No SQLite, classes beyond `Task`, or anything we haven't done yet
- Write the code yourself, without AI-generated code

## A finished product can

1. **Add** a task with a title and optional tags. Ids are unique and auto-assigned: one higher than the current highest id, or `1` if the list is empty
2. **List** all tasks, showing id, title, tags, and a done marker (`[x]` or `[ ]`), with unfinished tasks first
3. **Complete** a task by id
4. **Delete** a task by id
5. **Filter** by tag
6. **Show pending** tasks only
7. **Save automatically** after every change and **load automatically** on startup
8. **Start cleanly on first run** when no file exists yet
9. **Handle bad input** without crashing: an id that doesn't exist, an empty title, or a non-number typed where an id is expected
10. **Run from a menu loop** until the user chooses to quit

## Done when

You can add a few tasks, quit, rerun the script, and everything is still there with the right done states and tags. A deleted task's id is not reused by accident for a task that already exists, and nothing crashes on bad input.

When you're done, paste your code and I'll review it.
