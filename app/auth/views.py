from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, RegistForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.Username.data).first()
        if user is not None and user.verify_password(form.Password.data):
            login_user(user, form.rememberme.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
                flash('登入成功', 'success')
            return redirect(next)
        flash('錯誤的帳號或密碼!', 'error')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/regist', methods=['GET', 'POST'])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        user = User(email=form.Email.data, username=form.Username.data, password=form.Password.data)
        db.session.add(user)
        db.session.commit()
        flash('註冊成功!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/regist.html', form=form)
