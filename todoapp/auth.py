from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .extensions import db
import os


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')


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

    return render_template('auth/register.html')