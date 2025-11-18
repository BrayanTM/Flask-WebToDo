from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import functools
from .models import User
from .extensions import db
import os


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method=os.getenv('CRYPT_METHOD'))

        new_user = User(username=username, password=hashed_password)
        
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash(message='El nombre de usuario ya existe!', category='error')
            return redirect(url_for('auth.register'))
        
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully!', 'success')
        return redirect(url_for('auth.login'))

    if g.user:
        return redirect(url_for('todo.index'))
    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session.clear()
            session['user_id'] = user.id
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('todo.index'))
        else:
            flash('Nombre de usuario o contraseña inválidos', 'error')
    
    if g.user:
        return redirect(url_for('todo.index'))
    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
