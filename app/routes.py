from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import Task
from app.forms import TaskForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, status=form.status.data, deadline=form.deadline.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.index'))
    tasks = Task.query.all()
    return render_template('index.html', form=form, tasks=tasks)