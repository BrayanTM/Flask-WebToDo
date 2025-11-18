from flask import Flask, render_template
from dotenv import load_dotenv
import os

from .extensions import db
from . import todo, auth


load_dotenv()


def create_app():


    app = Flask(__name__)


    # Configuraciones de la aplicación
    app.config.from_mapping(
        DEBUG=os.getenv('DEBUG', 'False') == 'True',
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    )


    # Inicialización de extensiones
    db.init_app(app)

    # Registro de blueprints
    app.register_blueprint(todo.todo_bp)
    app.register_blueprint(auth.auth_bp)


    @app.route('/')
    def index():
        return render_template("index.html")
    

    with app.app_context():
        db.create_all()


    return app