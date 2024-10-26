from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from forms import LoginForm, RegisterForm
from app import db
from models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logic for authenticating user
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('user.dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html', form=form)