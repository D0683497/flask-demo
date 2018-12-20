from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, RegistForm, ChangePasswordForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
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
    flash('成功登出', 'warning')
    return redirect(url_for('main.index'))


@auth.route('/regist', methods=['GET', 'POST'])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, 
                    password=form.password.data,
                    name=form.name.data,
                    about=form.about.data,
                    location=form.location.data)
        db.session.add(user)
        db.session.commit()
        flash('註冊成功!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/regist.html', form=form)

@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            logout_user()
            flash('密碼更改成功，請重新登入', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('密碼輸入錯誤', 'error')
    return render_template("auth/change_password.html", form=form)