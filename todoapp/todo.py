from flask import Blueprint, render_template, request, url_for, redirect, flash, g
from todoapp.auth import login_required
from .models import TodoItem, User
from .extensions import db


todo_bp = Blueprint('todo', __name__, url_prefix='/todo')


@todo_bp.route('/list')
@login_required
def index():
    todo_items = TodoItem.query.all()
    return render_template('todo/index.html', todo_items=todo_items)


@todo_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')

        new_todo = TodoItem(user=g.user.id, title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()

        flash('Tarea agregada exitosamente!', 'success')
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')


@todo_bp.route('/update/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def update_task(todo_id):
    todo_item = TodoItem.query.get_or_404(todo_id)

    if request.method == 'POST':
        todo_item.title = request.form['title']
        todo_item.description = request.form.get('description', '')
        todo_item.completed = 'status' in request.form

        db.session.commit()

        flash('Tarea actualizada exitosamente!', 'success')
        return redirect(url_for('todo.index'))

    return render_template('todo/update.html', todo_item=todo_item)


@todo_bp.route('/delete/<int:todo_id>', methods=['POST'])
@login_required
def delete_task(todo_id):
    todo_item = TodoItem.query.get_or_404(todo_id)
    db.session.delete(todo_item)
    db.session.commit()
    flash('Tarea eliminada exitosamente!', 'success')
    return redirect(url_for('todo.index'))