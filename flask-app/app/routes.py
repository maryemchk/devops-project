# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from .services import get_all_tasks, create_task, remove_task

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        create_task(task)
        return redirect(url_for('main.home'))

    tasks = get_all_tasks()
    return render_template("home.html", tasks=tasks)

@main.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    remove_task(index)
    return redirect(url_for('main.home'))
