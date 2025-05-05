# app/models.py

tasks = []

def get_tasks():
    return tasks

def add_task(task):
    if task:
        tasks.append(task)

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
