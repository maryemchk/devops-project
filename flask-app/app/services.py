# app/services.py

from .models import get_tasks, add_task, delete_task

def get_all_tasks():
    return get_tasks()

def create_task(task_text):
    add_task(task_text)

def remove_task(index):
    delete_task(index)
