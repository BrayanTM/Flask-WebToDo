from flask import Flask, render_template
from . import todo, auth
from dotenv import load_dotenv
import os


load_dotenv()


def create_app():

    app = Flask(__name__)


    # Configuraciones de la aplicación
    app.config.from_mapping(
        DEBUG=os.getenv('DEBUG', 'False') == 'True',
        SECRET_KEY=os.getenv('SECRET_KEY'),
    )

    # Registro de blueprints
    app.register_blueprint(todo.todo_bp)
    app.register_blueprint(auth.auth_bp)


    @app.route('/')
    def index():
        return render_template("index.html")
    
    return app