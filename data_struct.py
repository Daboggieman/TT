from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    id: int
    title: str = "Task"
    done: bool = False
    tags: List[str] = field(default_factory = List)

def add_task(
title,
tags        
):
    pass

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