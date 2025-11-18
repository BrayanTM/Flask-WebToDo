from flask import Blueprint

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')

@todo_bp.route('/list')
def index():
    return "Aquí está la lista de tareas pendientes."


@todo_bp.route('/add')
def add_task():
    return "Aquí puedes agregar una nueva tarea pendiente."